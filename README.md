# Keylogger-with-Email-Sending-Functionality

## Description
This Python script captures keystrokes using the `pynput` library and periodically sends the recorded keystrokes to a specified email address using SMTP. The script runs in the background, collecting keystrokes and sending them via email every 10 seconds (default interval). It also includes logging functionality to track keypress activity.

---
## Features
- **Keystroke Logging:** Captures all keystrokes in real-time.
- **Email Reporting:** Sends recorded keystrokes to a specified email address at regular intervals.
- **Background Execution:** Runs as a background process.
- **Threading:** Uses threading to periodically send collected keystrokes.
- **Logging:** Maintains logs for keystroke activity tracking.

---
## Technologies Used
- **Python 3**
- **pynput:** For capturing keyboard input.
- **smtplib:** For sending keystroke logs via email.
- **email.mime:** To format emails with captured data.
- **threading:** For scheduling email sending in the background.
- **logging:** For tracking keystroke activity.

---
## Setup Instructions

### Prerequisites
- Python 3.x installed on your system.
- `pip` package manager installed.
- A valid email account for sending logs.

### Installation
1. Clone the repository or download the script.
   ```sh
   git clone https://github.com/Kernel-Freak/Keylogger-with-Email-Sending-Functionality
   cd Keylogger-with-Email-Sending-Functionality
   ```
2. Install required dependencies:
   ```sh
   pip install pynput
   ```
3. Update the script with your email credentials:
   ```python
   sender_email = "your_dummy_email@gmail.com"
   receiver_email = "your_receiver_email@example.com"
   password = "your_app_specific_password"
   ```

### Running the Application
Execute the following command in your terminal:
```sh
python keylogger.py
```
To stop the script, press the **Escape (ESC)** key.

---
## Security Measures
- **Email Authentication:** Uses secure SMTP authentication for email sending.
- **Thread Management:** Ensures efficient log collection and email sending without overloading resources.
- **Logging:** Maintains records of keystroke activity for analysis.

---
## Important Notes
- Ensure that your email provider allows SMTP access.
- The script should only be used for ethical and educational purposes.
- Unauthorized use of keyloggers can be illegal and violate privacy laws.

---
## Contributions
Contributions are welcome! Feel free to fork this repository and submit a pull request.

---
## Contact
For any queries or issues, please contact samratmandal423@gmail.com.

---
## License
This project is for **learning purposes only**. The author is not responsible for any misuse of this script.



