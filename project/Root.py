import tkinter as tk
from tkinter import messagebox



class main():
    def __init__(self):
        root = tk.Tk()
        root.title('O.S. PACKS')
        root.geometry('400x300')

        button = tk.Button(text="ddd", bg="black", fg="white")
        button.pack()

        root.mainloop()

main()