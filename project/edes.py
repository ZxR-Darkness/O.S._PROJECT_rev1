#  доп файл с созданием txt файлов для работы 

import tkinter as tk
import os

try:

    "здесь все файлы которые создавал проект можете ознакомится что там было"
    def filesave():
        secrets2 = open('project/secrets/DSD.txt','w')  # открытие в режиме записи   
        secrets2.write("его нету и не будет никогда.... ладно слушай скажу даже бог не знает что в этой проге ты можешь продолжить но я бы советовал уйти \n но если хочешь продолжить то вот (GIDS)")
        defing = tk.Tk()

        btn = tk.Button(defing, text="create file", command=filesave )
        btn.place_configure(x=23,y=23)

    def textone():
        secrets3 = open('project/secrets/empty.txt','w')  # открытие в режиме записи  
        secrets3.write("???: ты не видел куда босс клал ключ от ПК? \n ???: да всмысле ты не видел?! \n ???: ладно пофиг кароче иди ты нахуй я сам найду ;№*%___os dev___?;*(%)")
        secrets3.close  # закрытие для оптимизации кода
        
    def texttwo():
        secrets3 = open('project/secrets/ERROR.txt','w')  # открытие в режиме записи  
        secrets3.write("bot да что-то было вроде ?foxlolka?")
        secrets3.close  # закрытие для оптимизации кода

    def texttree():
        secrets3 = open('project/secrets/what.txt','w')  # открытие в режиме записи  
        secrets3.write("знаешь что? я не убивал тех кто зашел я лишь указал правильный им путь а дальше они сами решили....")
        secrets3.close # закрытие для оптимизации кода
    def textfour():
        secrets4 = open('Update.txt','w')  # открытие в режиме записи  
        secrets4.write("UPDATE 0.4.8")
        secrets4.close # закрытие для оптимизации кода
except(all):
    print("ошибка файлов")


# beta функции
# def beta_1():
#     try:
#         secrets5 = open("project/beta_folder/text.txt", 'w+')    # открытие в режиме чтения
#         secrets5.write("beta test file")
#         secrets5.read()
#         print(*secrets5)
#         secrets5.close  # закрытие для оптимизации кода
#     except(FileNotFoundError):
#         print("файл не найден")