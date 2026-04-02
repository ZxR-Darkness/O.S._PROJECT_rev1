#  доп файл с созданием txt файлов для работы 

import tkinter as tk
import os


def _ensure_dirs() -> None:
    os.makedirs('projects/secrets', exist_ok=True)


"здесь все файлы которые создавал проект можете ознакомится что там было"


def filesave() -> None:
    _ensure_dirs()
    with open('projects/secrets/DSD.txt', 'w', encoding='utf-8') as secrets2:
        secrets2.write(
            "его нету и не будет никогда.... ладно слушай скажу даже бог не знает что в этой проге ты можешь продолжить но я бы советовал уйти \n "
            "но если хочешь продолжить то вот secretTWO"
        )

    defing = tk.Tk()
    btn = tk.Button(defing, text="create file", command=filesave)
    btn.place_configure(x=23, y=23)


def textone() -> None:
    _ensure_dirs()
    with open('projects/secrets/empty.txt', 'w', encoding='utf-8') as secrets3:
        secrets3.write(
            "???: ты не видел куда босс клал ключ от ПК? \n ???: да всмысле ты не видел?! \n "
            "???: ладно пофиг кароче иди ты нахуй я сам найду ;№*%___os dev___?;*(%)"
        )


def texttwo() -> None:
    _ensure_dirs()
    with open('projects/secrets/ERROR.txt', 'w', encoding='utf-8') as secrets3:
        secrets3.write("bot да что-то было вроде ?? secret  ")


def texttree() -> None:
    _ensure_dirs()
    with open('projects/secrets/what.txt', 'w', encoding='utf-8') as secrets3:
        secrets3.write(
            "знаешь что? я не убивал тех кто зашел я лишь указал правильный им путь а дальше они сами решили...."
        )


def textfour() -> None:
    with open('Update.txt', 'w', encoding='utf-8') as secrets4:
        secrets4.write("UPDATE 0.5.0 beta")


def textfive() -> None:
    with open('New App.txt', 'w', encoding='utf-8') as secrets4:
        secrets4.write("а что ты тут забыл? хахаха ладно anomaly ")
