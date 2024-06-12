#главный файл
try:
    import pygame
    import progress

# except помогает вам сразу запустить программу в VSC так как он отвечает за установку нужных модулей
except ImportError:
    # Если модуль не найден, выполняется данный код
    import subprocess
    subprocess.check_call(["pip", "install", "pygame"])  # Установка модуля через pip
    subprocess.check_call(["pip", "install", "progress"])  # Установка модуля через pip
    import pygame  # Попытка импорта модуля снова
    import progress  # Попытка импорта модуля снова

import tkinter as tk
from tkinter import messagebox          #импорт нужных файлов и модулей
import traceback
import logging
from dlc import box
from dlc import texting
from dlc import radio
from dlc import baring
from dlc import crush
from dlc import testing2
from dlc import folders
# from edes import beta_1
from edes import filesave
from edes import textone
from edes import texttwo
from edes import textfour
try:
    #вызов нужных системных функций
    folders()
    baring() # загрузка в кмд
except Exception as e:
    logging.error(traceback.format_exc())

check = {'manto': "manto aio 80 kit", 'me': 'ты? ну ок'}
h = "XX ASCII"  # пока не используеться
Off = 23
def PRESS(): #ввод имени                                 пока не используеться
     global name2                                          
     name2 = entry2.get()
     return name2

# чтобы изменить команды для активации вам нужно в строке elif == "" в ковычках внести свое слово тогда это будет слово активации
# после снизу отступ и можете вписывать свои нужный слова или фунции для вывода используйте printing(tk.END, "") тоже в ковычках впишите
# нужные вам с лова вывода!
try:
    def main():
        printing = output.insert
        guess = entry.get()
        guess2 = entry2.get()
        output.delete(1.0, tk.END)  # Очищаем поле вывода перед новым выводом
        if guess == "help":                                                                 #некоторые приколы а также спец. слова для использования других секреток
            output.insert(tk.END, 'команды: me, manto, drag 2, aegis, help me, kill you, ????, сука, молчи (нинада), hell, update 8, darkness, GIDS')

        # elif guess == "realese":
        #     printing(tk.END, "дада релиз")

        elif guess == 'привет':
            printing(tk.END, f"{PRESS()} привет!")
            texting()
        
        elif guess == 'пока':
            printing(tk.END, f"{PRESS()} возврайщайся!")
            
        elif guess == 'me': #прикольчик
            printing(tk.END, 'ты? ну ок')
            textone()

        elif guess == check:
            print(check)
        elif guess == 'manto': #прикольчик

            printing(tk.END, 'manto aio 80 kit')

        elif guess == 'foxlolka':
            printing(tk.END, 'секретный файл разблокирован')
            textone()
        elif guess == "drag 2": #прикольчик
            printing(tk.END, 'drag 2 ичо дальше?')

        elif guess2 == "memento mori":
            printing(tk.END, "не надо о ней помнить она сама напомнит о себе...")
            output2.insert(tk.END, "не надо о ней помнить она сама напомнит о себе...")

        elif guess == "aegis": #прикольчик
            printing(tk.END,'tkaegis boost 2')

        elif guess == 'hell': #прикольчик
            printing(tk.END, 'мм а ты любишь погоречей')
        
        elif guess == 'как дела':
            printing(tk.END, "нормально а у тебя?")

        elif guess == 'good place':
            printing(tk.END, "yeah you know english wow")
        
        elif guess == "сука": #прикольчик
            PRESS()
            printing(tk.END, f'{name2} ты совсем офигел?')
        elif guess == "молчи": #прикольчик

            printing(tk.END,'окей команда принята пооокааа')
            baring()
            crush()

        elif guess == 'help me':
            baring()          
            x = open('ERROR.txt', 'rt') # файл txt в котором что-то есть
            sms = x.read()              # сам хз что там
            printing(tk.END, sms)
        
        elif guess2 == "SECURE":
            box()

        elif guess == "kill you":                                           
            PRESS()                                                        
            printing(tk.END, f"{name2} ты идиот")                                                                                   


        elif guess == "god":
            printing(tk.END, 'пожалуйста подождите...')
            filesave()

        elif guess == "bot":
            printing(tk.END, "hm bot tg? он хранит много тайн")
            gosa()
        elif guess == "secret": # секрет
            radio()
            btn8 = tk.Button(text='не нажимай я прошу тебя открой файл ERROR', command=testing2)
            btn8.pack
        
        elif guess == "anomaly":
            printing(tk.END , "oh god, give me my camer")
            output2.insert(tk.END, "EERERERERERE anomale mara shmara erererererer")
            print(":3")
        elif guess == "новый год":
            printing(tk.END, "С НОВЫМ ГОДОМ 2024!!!")
        
        elif guess == "GIDS":
            printing(tk.END, "ты что делаешь?")
            texttwo()
        
        elif guess == "TEST":
            printing(tk.END, "TEST TEST TEST TEST")

        elif guess == "DARKNESS":
            printing(tk.END, "а может все таки нет? \n версия 0.4.8 все таки выходит похоже")

        elif guess == "update 4.9":
            printing(tk.END, "O.S. PROJECT 0.4.9")

        elif guess == "os dev":
            printing(tk.END, "хм интересно")
            textfour()
        
        # elif guess == "beta":
        #     printing("test test test")
        #     beta_1()


        else:
            printing(tk.END, "неправильная команда")
        def gosa():
            printing(tk.END, f"{name2} прими то что ты не можешь принять")

except(all):
    print("ошибка команд")



window = tk.Tk()       # создает окно с кодом
window.configure(background='black')
#window.iconbitmap('C:\codes2\project\img\Python.ico')            
# Создаем виджеты
label = tk.Label(window, text="введи что-нибудь:")                                  # виджеты кнопки, поле для ввода, само окно
label.configure(background="black", fg='white')
label.grid_configure(row=10,column=10)

entry = tk.Entry(window)
entry.grid_configure(row=20,column=10)

label2 = tk.Label(window, text="имя:")
label2.configure(background="black", fg='white')
label2.grid_configure(row=30,column=10)

entry2 = tk.Entry(window)                                                     
entry2.grid_configure(row=40,column=10)

button = tk.Button(window, text="Ввод", command=main)
button.configure(background="black", fg='white')
button.grid_configure(row=50,column=10)

output = tk.Text(window) 
output.configure(background="black", fg='red')
output.grid_configure(row=60,column=10)
#2
output2 = tk.Text(window)
output2.configure(background="black", fg='white')
output2.grid_configure(row=70,column=10)
output.insert(tk.END, "чтобы увидеть все команды напиши helр, также сперва впиши имя, предупреждаю что программа может выключать компьютер \n пожалуйста запускайте когда будете готовы \n \n v0.4.9 beta") # надпись в начале
window.mainloop()
