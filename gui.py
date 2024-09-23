from tkinter import *
from tkinter import ttk
import tkinter as tk

root = Tk()
root.geometry("1920x1080")
root.config(background="Grey")
judul = Label(
    text="Cloathing Bussinnes Analysis",
    background="Grey",
    font=("Arial", 20, "bold"),
)
judul.place(relx=0.5, rely=0.15)
ext = Button(text="Exit", font=("Arial", 20), width=12)
ext.place(relx=0.05, rely=0.15)

modal_text = Label(text="Modal")
modal_text.place(relx=0.05, rely=0.15)
modal_entry = Entry(root, width=37, background="White")
modal_text.place(relx=0.05, rely=0.3)
root.mainloop()
