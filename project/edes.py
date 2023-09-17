import tkinter as tk


def filesave():
    secrets2 = open('DSD.txt','w')  # открытие в режиме записи  # не используеться в данный момент
    secrets2.write("его нету и не будет никогда god")
    defing = tk.Tk()

    btn = tk.Button(defing, text="create file", command=filesave )
    btn.place_configure(x=23,y=23)

def textone():
    secrets3 = open('DSD.txt','w')  # открытие в режиме записи  # не используеться в данный момент
    secrets3.write("слушай а ты хитрый ладно дам тебе один прикол god дамн")

