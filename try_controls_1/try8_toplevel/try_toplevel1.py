# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

# ------------------------------

def create_subwin():
    sub_win = tk.Toplevel(top_win)
    sub_win.title('Python')
    #sub_win.attributes('-alpha',0.5)

    msg = tk.Message(sub_win, text='I love study')
    msg.pack()
    return

btn_create = tk.Button(top_win, text='Create a sub win', command=create_subwin)
btn_create.pack()
# ------------------------------


# show window and get into event loop
top_win.mainloop()
