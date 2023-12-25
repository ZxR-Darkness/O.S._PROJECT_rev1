#главный файл
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
from dlc import exttree
texttwo()
baring() # загрузка в кмд
texting()

check = {'manto': "manto aio 80 kit", 'me': 'ты? ну ок'}
h = "XX ASCII"  # пока не используеться
Off = 23
def PRESS(): #ввод имени                                 пока не используеться
     global name2                                          
     name2 = entry2.get()

def main():
    guess = entry.get()
    guess2 = entry2.get()
    output.delete(1.0, tk.END)  # Очищаем поле вывода перед новым выводом
    if guess == "help":                                                                 #некоторые приколы а также спец. слова для использования других секреток
        output.insert(tk.END, 'команды: me, manto, drag 2, aegis, help me, kill you, god, сука, молчи (нинада), hell')   #также приколы и секреты будут отделены друг от друга 

    elif guess == 'привет':
        output.insert(tk.END, f"{name2} привет!")
    
    elif guess == 'пока':
        output.insert(tk.END, f"{name2} возврайщайся!")
        
    elif guess == 'me': #прикольчик
        output.insert(tk.END, 'ты? ну ок')

    elif guess == check:
        print(check)
    elif guess == 'manto': #прикольчик

        output.insert(tk.END, 'manto aio 80 kit')

    elif guess == 'foxlolka':
        output.insert(tk.END, '')
        textone()
    elif guess == "drag 2": #прикольчик
        output.insert(tk.END, 'drag 2 ичо дальше?')

    elif guess2 == "memento mori":
        output.insert(tk.END, "не надо о ней помнить она сама напомнит о себе...")
        output2.insert(tk.END, "не надо о ней помнить она сама напомнит о себе...")

    elif guess == "aegis": #прикольчик
         output.insert(tk.END,'tkaegis boost 2')

    elif guess == 'hell': #прикольчик
        output.insert(tk.END, 'мм а ты любишь погоречей')
    
    elif guess == 'как дела':
        output.insert(tk.END, "нормально а у тебя?")

    elif guess == 'good place':
        output.insert(tk.END, "yeah you know english wow")
    
    elif guess == "сука": #прикольчик
        PRESS()
        output.insert(tk.END, f'{name2} ты совсем офигел?')
    elif guess == "молчи": #прикольчик

        output.insert(tk.END,'окей команда принята пооокааа')
        baring()
        crush()

    elif guess == 'help me':
        baring()          
        x = open('ERROR.txt', 'rt') # файл txt в котором что-то есть
        sms = x.read()              # сам хз что там
        output.insert(tk.END, sms)
    
    elif guess2 == "SECURE":
        box()

    elif guess == "kill you":                                           
         PRESS()                                                        
         output.insert(tk.END, f"{name2} ты идиот")                                                                                   


    elif guess == "god":
        output.insert(tk.END, 'пожалуйста подождите...')
        filesave()

    elif guess == "bot":
        output.insert(tk.END, "hm bot tg? он хранит много тайн")
        gosa()
    elif guess == "secret": # секрет
        radio()
        btn8 = tk.Button(text='не нажимай я прошу тебя открой файл ERROR', command=testing2)
        btn8.pack

    elif guess == "restart":
        baring()
        print("O.S. PROJECT 2.0")
        output.insert(tk.END, "O.S. project 2.0    2024")
    
    elif guess == "anomaly":
        output.insert(tk.END , "oh god, give me my camer")
        output2.insert(tk.END, "EERERERERERE anomale mara shmara erererererer")
        print(":3")

    elif guess2 == "foxlolka":
        output2.insert(tk.END, "darkness?")

    else:
        output.insert(tk.END, "неправильная команда")
    def gosa():
        output.insert(tk.END, f"{name2} прими то что ты не можешь принять")


window = tk.Tk()       # создает окно с кодом
window.iconbitmap('C:\codes2\project\img\Python.ico')            
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
output.insert(tk.END, "чтобы увидеть все команды напиши helр, также сперва впиши имя, предупреждаю что программа может выключать компьютер \n пожалуйста запускайте когда будете готовы \n v0.4.4") # надпись в начале
window.mainloop()