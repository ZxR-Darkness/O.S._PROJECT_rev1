#  доп файл с созданием txt файлов для работы 

import tkinter as tk

def filesave():
    secrets2 = open('DSD.txt','w')  # открытие в режиме записи   
    secrets2.write("его нету и не будет никогда god")
    defing = tk.Tk()

    btn = tk.Button(defing, text="create file", command=filesave )
    btn.place_configure(x=23,y=23)

def textone():
    secrets3 = open('DSD.txt','w')  # открытие в режиме записи  
    secrets3.write("слушай а ты хитрый ладно дам тебе один прикол god дамн")

def texttwo():
    secrets3 = open('DSD.txt','w')  # открытие в режиме записи  
    secrets3.write("bot да что-то было вроде")

def texttree():
    secrets4 = open('ПРОЧИТАЙ СРОЧНО.txt','w')  # открытие в режиме записи  
    secrets4.write("послушай я не знаю что происходит разберись тут сам ладно я не знаю что это за обновление ведь 0.4.2 последние а тут 0.4.3.....")

