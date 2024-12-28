# IRCTC Booking Automation

This project automates the process of booking train tickets on the [IRCTC website](https://www.irctc.co.in/nget/train-search) using Selenium and Python. It includes functionality to log in, fill out journey details, solve captchas, and complete the booking process.

## Video Demonstration
https://github.com/user-attachments/assets/47bbb137-4dc8-4d6e-895f-198774ac0fc6

## Features
- Automated login with username and password.
- Automated captcha handling function.
- Input journey details: origin, destination, date, and booking type.
- Automatically select train, class, and seat.
- Fill passenger details and proceed to payment.

## Prerequisites
1. Install Python (3.7 or later).
2. Install Google Chrome and download the corresponding [ChromeDriver](https://chromedriver.chromium.org/).
3. Install required Python libraries:
   ```bash
   pip install selenium opencv-python numpy
   ```

## Local Setup

### Step 1: Clone the Repository
Clone the project repository from GitHub:

```bash
git clone https://github.com/yourusername/irctc-booking-automation.git
cd irctc-booking-automation
```

### Step 2: Set Up ChromeDriver
Download ChromeDriver for your version of Chrome and place it in the project directory. Update the path in the script if necessary.

### Step 3: Install Dependencies
Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```

### Step 4: Add Your Credentials
Update the `username` and `pwd` variables in the script with your IRCTC login credentials.

### Step 5: Run the Script
Execute the script using Python:

```bash
python irctc_automation.py
```

## Files
- **irctc_automation.py**: Main script for automation.
- **detect.py**: Contains the function for solving captchas.
- **video/**: Folder containing a demonstration video of the automation.
- **requirements.txt**: Lists the required Python libraries.

## Notes
- Ensure your IRCTC credentials and journey details are correctly updated in the script.
- The script uses ChromeDriver; update the version if your Chrome browser updates.
- Some captchas may not be solvable automatically due to complexity. Adjust the `bringbro` function if needed.

## Contributing
Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/yourusername/irctc-booking-automation/issues).

---

Feel free to star the repository if you find this project helpful!
