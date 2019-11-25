# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk

# tk._test()  # 测试 tkinter 是否正常工作

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
top_win.geometry(win_size_pos)

# Place number1
lbl_num1 = tk.Label(
    top_win,
    text='N1',
)
# lbl_num1.pack()
lbl_num1.place(
    x=20,
    y=20,
    width=20,
    height=20,
    anchor='nw'
)

# Place entry1
entry_num1 = tk.Entry(
    top_win,
    show=None,
)  # 显示成明文形式
entry_num1.place(
    x=40,
    y=20,
    width=40,
    height=20,
    anchor='nw'
)

# Place number2
lbl_num2 = tk.Label(
    top_win,
    text='N2',
)


# lbl_num2.pack()
lbl_num2.place(
    x=160,
    y=20,
    width=20,
    height=20,
    anchor='nw'
)

# Place entry2
entry_num2 = tk.Entry(
    top_win,
    show=None,
)  # 显示成明文形式
entry_num2.place(
    x=180,
    y=20,
    width=40,
    height=20,
    anchor='nw'
)


# show window and get into event loop
top_win.mainloop()
