import tkinter as tk
from tkinter import messagebox          #импорт нужных файлов и модулей
from dlc import box
from dlc import texting
from dlc import radio
from dlc import baring
from dlc import crush
from edes import filesave
from edes import textone

baring() # загрузка в кмд
texting() 
frazes = {"fox" : "fox lol ahaha"} # пока не используеться
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
                                                       
    elif guess == 'me': #прикольчик
        output.insert(tk.END, 'ты? ну ок')


    elif guess == 'manto': #прикольчик

        output.insert(tk.END, 'manto aio 80 kit')

    elif guess == 'foxlolka':
        output.insert(tk.END, '')
        textone()
    elif guess == "drag 2": #прикольчик

        output.insert(tk.END, 'drag 2 ичо дальше?')

    elif guess == "aegis": #прикольчик
         output.insert(tk.END,'tkaegis boost 2')

    elif guess == 'hell': #прикольчик
        output.insert(tk.END, 'мм а ты любишь погоречей')
    
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

    elif guess == "kill you":                                            # эти строки должны быть началом того что я делаю
         PRESS()                                                          # но есть проблемы это то что весь этот код запускаеться 
         output.insert(tk.END, f"{name2} ты идиот")                       # в другом коде из-за hello.risk2() пытаюсь эт исправить так что половина кода там                                                                   # НО в данный момент можно запустить с этого кода
 

    elif guess == "god":
        output.insert(tk.END, 'пожалуйста подождите...')
        filesave()

    elif guess == "secret": # секрет
        radio()
    
    
    
    else:
        output.insert(tk.END, "неправильная команда")
    


window = tk.Tk()       # создает окно с кодом
window.iconbitmap('C:\codes2\project\img\Python.ico')      
#        
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

output2 = tk.Text(window)
output2.pack()
output.insert(tk.END, "чтобы увидеть все команды напиши helр, также сперва впиши имя") # надпись в начале
window.mainloop()                                                                                                  # upd v0.4.0 coming soon...