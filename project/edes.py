#  доп файл с созданием txt файлов для работы 

import tkinter as tk

def filesave():
    secrets2 = open('DSD.txt','w')  # открытие в режиме записи   
    secrets2.write("его нету и не будет никогда.... ладно слушай скажу даже бог не знает что в этой проге ты можешь продолжить но я бы советовал уйти \n но если хочешь продолжить то вот (GIDS)")
    defing = tk.Tk()

    btn = tk.Button(defing, text="create file", command=filesave )
    btn.place_configure(x=23,y=23)

def textone():
    secrets3 = open('DSD2.txt','w')  # открытие в режиме записи  
    secrets3.write("???: ты не видел куда босс клал ключ от ПК? \n ???: да всмысле ты не видел?! \n ???: ладно пофиг кароче иди ты нахуй я сам найду ;№*%?;*(%)")

def texttwo():
    secrets3 = open('Dsd3.txt','w')  # открытие в режиме записи  
    secrets3.write("bot да что-то было вроде")

def texttree():
    secrets3 = open('files2.txt','w')  # открытие в режиме записи  
    secrets3.write("знаешь что? я не убивал тех кто зашел я лишь указал правильный им путь а дальше они сами решили....")
