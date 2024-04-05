#главный файл
try:
    import pygame
    import progress
except ImportError:
    # Если модуль не найден, выполняется данный код
    import subprocess
    subprocess.check_call(["pip", "install", "pygame"])  # Установка модуля через pip
    subprocess.check_call(["pip", "install", "progress"])  # Установка модуля через pip
    import pygame  # Попытка импорта модуля снова
    import progress  # Попытка импорта модуля снова

import tkinter as tk
from tkinter import messagebox          #импорт нужных файлов и модулей
from dlc import box
from dlc import texting
from dlc import radio
from dlc import baring
from dlc import crush
from dlc import testing2
from edes import filesave
from edes import textone
from edes import texttwo


texttwo()
baring() # загрузка в кмд
texting()


check = {'manto': "manto aio 80 kit", 'me': 'ты? ну ок'}
h = "XX ASCII"  # пока не используеться
Off = 23
def PRESS(): #ввод имени                                 пока не используеться
     global name2                                          
     name2 = entry2.get()

# чтобы изменить команды для активации вам нужно в строке elif == "" в ковычках внести свое слово тогда это будет слово активации
# после снизу отступ и можете вписывать свои нужный слова или фунции для вывода используйте printing(tk.END, "") тоже в ковычках впишите
# нужные вам с лова вывода!
def main():
    printing = output.insert
    guess = entry.get()
    guess2 = entry2.get()
    output.delete(1.0, tk.END)  # Очищаем поле вывода перед новым выводом
    if guess == "help":                                                                 #некоторые приколы а также спец. слова для использования других секреток
        output.insert(tk.END, 'команды: me, manto, drag 2, aegis, help me, kill you, ????, сука, молчи (нинада), hell')   #также приколы и секреты будут отделены друг от друга 

    # elif guess == "realese":
    #     printing(tk.END, "дада релиз")

    elif guess == 'привет':
        printing(tk.END, f"{name2} привет!")
    
    elif guess == 'пока':
        printing(tk.END, f"{name2} возврайщайся!")
        
    elif guess == 'me': #прикольчик
        printing(tk.END, 'ты? ну ок')
        textone()

    elif guess == check:
        print(check)
    elif guess == 'manto': #прикольчик

        printing(tk.END, 'manto aio 80 kit')

    elif guess == 'foxlolka':
        printing(tk.END, '')
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

    elif guess2 == "foxlolka":
        output2.insert(tk.END, "закрыто к сожалению он больше не занимается проектом....")
    
    
    elif guess == "GIDS":
        printing(tk.END, "ты что делаешь?")
        texttwo()
    
    elif guess == "TEST":
        printing(tk.END, "TEST TEST TEST TEST")

    else:
        printing(tk.END, "неправильная команда")
    def gosa():
        printing(tk.END, f"{name2} прими то что ты не можешь принять")

window = tk.Tk()       # создает окно с кодом
#window.iconbitmap('C:\codes2\project\img\Python.ico')            
# Создаем виджеты
label = tk.Label(window, text="введи что-нибудь:")                                   # виджеты кнопки, поле для ввода, само окно
label.pack()

entry = tk.Entry(window)
entry.pack()

label2 = tk.Label(window, text="имя:")
label2.pack()

entry2 = tk.Entry(window)                                                     
entry2.pack()

button = tk.Button(window, text="Ввод", command=main)
button.pack()

output = tk.Text(window) 
output.pack()
#2
output2 = tk.Text(window)
output2.pack()
output.insert(tk.END, "чтобы увидеть все команды напиши helр, также сперва впиши имя, предупреждаю что программа может выключать компьютер \n пожалуйста запускайте когда будете готовы \n \n к сожалению это последния версия я очень надеюсь что кто-то продолжит мой проект \n и сделает его полным \n \n v0.4.6-alpha") # надпись в начале
window.mainloop()
#лишь подготвка