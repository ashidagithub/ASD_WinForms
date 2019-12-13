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
# blablabla
def cmd_menu_item():
    tk.messagebox.showinfo(title='Information',
                           message='Menu clicked !')  # 提示信息对话窗
    return

# create a top menu
menubar = tk.Menu(top_win)
menubar.add_command(label="Hello", command=cmd_menu_item)
menubar.add_command(label="Quit", command=top_win.quit)

# show the menu
top_win.config(menu=menubar)


# ------------------------------


# show window and get into event loop
top_win.mainloop()
