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
frame_root1 = tk.Frame(top_win, bg="grey", width=760, height=300)
# frame_root1.pack()
frame_root1.place(x=20, y=20)


# Step2: Appedn other controls
# 单选框

'''
需要先定义tkinter里的变量：var_sel = Intvar()
var_sel.set(),设置默认值
var_sel.get()，获取选中的值
'''
var_sel = tk.IntVar()
var_sel.set(1)  # default value

def show_selected():
    print(var_sel.get())
    return

radio_btn1 = tk.Radiobutton(frame_root1, text="one", value=1, variable=var_sel, bg="blue", command=show_selected)
radio_btn1.grid(row=0, column=0)

radio_btn2 = tk.Radiobutton(frame_root1, text="two", value=2, variable=var_sel, bg="blue", command=show_selected)
radio_btn2.grid(row=0, column=1)

radio_btn3 = tk.Radiobutton(frame_root1, text="three", value=3, variable=var_sel, bg="blue", command=show_selected)
radio_btn3.grid(row=0, column=2)


# show window and get into event loop
top_win.mainloop()
