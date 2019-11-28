# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Radio Button )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# tk._test()  # 测试 tkinter 是否正常工作

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
top_win.geometry(win_size_pos)

sb = tk.Scrollbar(top_win)
sb.pack(side='right', fill='y')

lb = tk.Listbox(top_win, yscrollcommand=sb.set)
for i in range(1000):
    lb.insert('end', str(i))

lb.pack(side='left', fill='both')
sb.config(command=lb.yview)

# show window and get into event loop
top_win.mainloop()
