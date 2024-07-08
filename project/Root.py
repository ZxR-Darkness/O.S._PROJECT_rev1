import tkinter as tk
from tkinter import messagebox



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