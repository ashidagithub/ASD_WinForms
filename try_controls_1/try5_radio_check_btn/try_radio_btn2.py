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


# Step1: Create frame
frame_root1 = tk.Frame(top_win, bg="grey", width=760, height=500)
# frame_root1.pack()
frame_root1.place(x=20, y=20)

# Step2: Appedn other controls
# 单选框
var_sel = tk.IntVar()
var_sel.set(1)
text_of_btn = ('Python', 'Java', 'C#', 'C++')

for idx in range(4):
    '''
    tk.Radiobutton(frame_root1, variable=var_sel,
                   text=text_of_btn[idx], value=idx).pack()
    '''
    rtn = tk.Radiobutton(frame_root1, variable=var_sel,
                         text=text_of_btn[idx], value=idx)
    rtn.place(x=20 + idx * 190, y=40)

print(var_sel.get())

# show window and get into event loop
top_win.mainloop()
