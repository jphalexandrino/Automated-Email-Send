import yfinance as yf
import matplotlib.pyplot as plt
import pyautogui
import pyperclip
import time

yf.Ticker("MSFT").history("5d")

ticker = input("Qual ação você quer acompanhar: ")
dados = yf.Ticker(ticker).history("6mo")
fechamento = dados.Close
fechamento.plot()

maxima = round(fechamento.max(), 2)
minima = round(fechamento.min(), 2)
atual = round(fechamento[-1], 2)

print(maxima)
print(minima)
print(atual)

pyautogui.PAUSE = 2 # tempo entre uma ação e outra (delay)

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

pyperclip.copy("exemple@gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("tab")

# Cria a mensagem formatada
mensagem = f"""
    Prezado gestor,

    Seguem, conforme solicitado, as análises dos últimos seis meses da ação {ticker}.

    Cotação máxima: R$ {maxima}
    Cotação mínima: R$ {minima}
    Cotação atual: R$ {atual}

    Qualquer dúvida, fico à disposição!

    Atte,
    Assinatura: João Pedro Hack 
"""

# Copia a mensagem para a área de transferência
pyperclip.copy(mensagem)

pyautogui.hotkey("ctrl", "v")
pyautogui.hotkey("ctrl", "enter")

    
print("E-mail enviado com sucesso!")

# comando para pegar a posição do mouse com delay de 5 segundos
time.sleep(5)
pyautogui.position()

'''
%pip install yfinance
%pip install matplotlib
%pip install pyautogui
%pip install pyperclip
'''