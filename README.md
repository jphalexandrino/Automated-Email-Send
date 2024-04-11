# Automated Email Send

## Description
The Automated Email Send script automates the process of sending email reports on stock market data. It navigates through the browser using keyboard commands to fetch and analyze the stock data of a chosen application (e.g., MSFT) from Yahoo Finance. Currently, the script compiles a report of the maximum, minimum, and current values of the stock over the last 6 months and sends it via email. The recipient email address needs to be directly specified in the code.

## Dependencies
- [yfinance](https://pypi.org/project/yfinance/): `pip install yfinance`
- [matplotlib](https://pypi.org/project/matplotlib/): `pip install matplotlib`
- [pyautogui](https://pypi.org/project/PyAutoGUI/): `pip install pyautogui`
- [pyperclip](https://pypi.org/project/pyperclip/): `pip install pyperclip`

## Prerequisites
- Gmail account: The script requires you to be logged into your Gmail account.
- Browser positioning: Ensure that the browser window is in the first position on the taskbar.

## Usage
1. Install the required dependencies using the provided pip commands.
2. Ensure you are logged into your Gmail account.
3. Position the browser window as the first item on the taskbar.
4. Modify the script to specify the desired stock application and recipient email address.
5. Run the script.

## Notes
- Ensure that you have Python installed on your system.
- Make sure to review and understand the code before running it.
- This script assumes a stable internet connection for fetching stock data.
- Modify the email content and formatting as per your requirements.

## Author
- Username: sondercs

Feel free to reach out for any questions or suggestions!
