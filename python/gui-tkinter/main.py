import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Hello")
root.geometry("600x400")

ttk.Label(root, text="Hello world!").pack()

root.mainloop()