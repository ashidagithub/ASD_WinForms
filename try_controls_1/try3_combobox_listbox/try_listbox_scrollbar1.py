# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Listbox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

'''
selectmode
判断多少项目可以选择,鼠标拖动如何影响选择:
BROWSE: 通常情况下,你只能选择一条线,一个ListBox。
如果您单击一个项目,然后拖动到不同的线路,选择将跟随鼠标。这是默认.
SINGLE: 你只能选择一条线,你可以拖不mouse.wherever的您单击按钮1,该行被选中.
MULTIPLE: 你可以选择任何的行数一次。点击任何行切换是否被选中.
EXTENDED: 你可以选择任何一次行相邻组的第一行上点击并拖动到最后一行.
'''
sb = tk.Scrollbar(top_win)
sb.place(x=60, y=20, height=500)

lb = tk.Listbox(top_win, selectmode=tk.BROWSE, yscrollcommand=sb.set)
for i in range(50):
    lb.insert('end', '%03d' % i)
#lb.pack(side='left', fill='both')
lb.place(x=20, y=20, width=40, height=500)
# connect sb & lb
sb.config(command=lb.yview)


# show window and get into event loop
top_win.mainloop()
