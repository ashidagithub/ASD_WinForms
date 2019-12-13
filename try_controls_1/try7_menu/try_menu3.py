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

#------------------------------

def cmd_undo():
    tk.messagebox.showinfo(title='Info',message='Undo sth.')  # 提示信息对话窗
    return

def cmd_redo():
    tk.messagebox.showinfo(title='Info',message='Redo sth.')  # 提示信息对话窗
    return

menubar = tk.Menu(top_win)
menubar.add_command(label='Undo', command=cmd_undo)
menubar.add_command(label='Redo', command=cmd_redo)

frame = tk.Frame(top_win, width=512, height=512,bg='red')
frame.pack()

def popup(event):
    menubar.post(event.x_root, event.y_root)

frame.bind("<Button-3>", popup)




#------------------------------

# show window and get into event loop
top_win.mainloop()
