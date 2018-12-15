import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image

class App(object):
    def __init__(self, master, **kwargs):
        self.master = master
        self.master.geometry("900x360")
        self.show_image()
        self.show_menu()

    def show_image(self):
        self.frame = tk.Frame(self.master, height=640, width=360)
        b = tk.Button(self.frame)
        image = ImageTk.PhotoImage(file="data/paths0.png")
        b.config(image=image)
        b.image = image
        b.pack(side="top")
        self.frame.pack(side="left")



    def show_menu(self):
        fm = tk.Frame(self.master)
        tk.Button(fm, text='Search', command=self.play_by_filters).pack(side="top")#, anchor=W, fill=X, expand=YES)
        tk.Button(fm, text='Reset Filters', command=self.play_by_filters).pack(side="top")#, anchor=W, fill=X, expand=YES)
        fm.pack(side="right")#, fill=BOTH, expand=YES)

    def play_by_filters(self):
        print("Some........")


root = tk.Tk()
app = App(root)
root.mainloop()