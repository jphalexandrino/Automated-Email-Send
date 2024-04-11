import yfinance as yf
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
import time

yf.Ticker("MSFT").history("5d")

ticker = input("Which stock do you want to track: ")
data = yf.Ticker(ticker).history("6mo")
closing_prices = data.Close
closing_prices.plot()

maximum = round(closing_prices.max(), 2)
minimum = round(closing_prices.min(), 2)
current = round(closing_prices[-1], 2)

print(maximum)
print(minimum)
print(current)

pyautogui.PAUSE = 2 # time between actions (delay)

pyautogui.hotkey("win", "d")
pyautogui.hotkey("win", "1")
pyautogui.hotkey("ctrl", "t")

pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("enter")
pyautogui.hotkey("tab") #1
pyautogui.hotkey("tab") #2
pyautogui.hotkey("tab") #3
pyautogui.hotkey("tab") #4
pyautogui.hotkey("tab") #5
pyautogui.hotkey("tab") #6
pyautogui.hotkey("tab") #7
pyautogui.hotkey("tab") #8
pyautogui.hotkey("tab") #9
pyautogui.hotkey("tab") #10
pyautogui.hotkey("tab") #11
pyautogui.hotkey("tab") #12
pyautogui.hotkey("enter")

pyperclip.copy("example@gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy("Daily Analysis")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Create formatted message
message = f"""
    Dear manager,

    Following your request, here are the analyses of the last six months for the {ticker} stock.

    Maximum price: $ {maximum}
    Minimum price: $ {minimum}
    Current price: $ {current}

    If you have any questions, feel free to ask!

    Regards,
    Signature: João Pedro Hack 
"""

# Copy message to clipboard
pyperclip.copy(message)

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

print("Email sent successfully!")

# command to get mouse position with 5 seconds delay
time.sleep(5)
pyautogui.position()
