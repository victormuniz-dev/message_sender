import pywhatkit as kit
import time
import pyautogui

numbers = [] #Coloque os números aqui


for number in numbers:
    kit.sendwhatmsg_instantly(number,
       "Mensagem a ser enviada")
    time.sleep(15)
    pyautogui.press('enter')