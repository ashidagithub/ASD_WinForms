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
# 复选框
text_of_btn = ('北京', '上海', '广州', '深圳')
v1 = tk.IntVar()
v2 = tk.IntVar()
v3 = tk.IntVar()
v4 = tk.IntVar()
value_of_btn = (v1, v2, v3, v4)


def show_selected():
    print('---')
    for v in value_of_btn:
        print(v.get())
    return


for idx in range(4):
    chk_btn = tk.Checkbutton(
        frame_root1,
        text=text_of_btn[idx],
        variable=value_of_btn[idx],
        command=show_selected
        )
    chk_btn.place(x=20 + idx * 190, y=40)


# show window and get into event loop
top_win.mainloop()
