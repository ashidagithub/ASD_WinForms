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
                           message='Menu item clicked !')  # 提示信息对话窗
    return

# create a top menu
top_menu = tk.Menu(top_win)
#top_menu.add_command(label="Hello", command=cmd_menu_item)
#top_menu.add_command(label="Quit", command=top_win.quit)

# Create first dropdown menu
filemenu = tk.Menu(top_menu, tearoff=False)
filemenu.add_command(label="Open", command=None)
filemenu.add_command(label="Save", command=None)
filemenu.add_separator()
filemenu.add_command(label="Quit", command=top_win.quit)
# add dropdown menu1 to top menu
top_menu.add_cascade(label="File", menu=filemenu)

# Create second dropdown menu
filemenu = tk.Menu(top_menu, tearoff=False)
filemenu.add_command(label="Select All", command=cmd_menu_item)
filemenu.add_separator()
filemenu.add_command(label="Copy", command=cmd_menu_item)
filemenu.add_command(label="Cut", command=cmd_menu_item)
filemenu.add_command(label="Paste", command=cmd_menu_item)
# add dropdown menu1 to top menu
top_menu.add_cascade(label="Edit", menu=filemenu)



# show the menu
top_win.config(menu=top_menu)

# ------------------------------


# show window and get into event loop
top_win.mainloop()
