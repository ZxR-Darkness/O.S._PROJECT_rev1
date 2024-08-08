import tkinter as tk
from tkinter import messagebox

# нароботки ZxR_Darkness
# "в планах было добавить не только одно основное окно"
# "второе окно было-бы как numpad для pin-code например чтобы искать более глубокие секреты проекта"
class main():
    def __init__(self):
        root = tk.Tk()
        root.title('O.S. PACKS')
        root.geometry('400x400')
        root["bg"] = "black"

        text1 = tk.Label(text="text text text", bg="red", fg="white")
        text1.pack()

        button = tk.Button(text="Button", bg="black", fg="white")
        button.pack()

        root.mainloop()

main()

"к сожалению мои руки не дошли до того чтобы реализовать это"