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

prog_total = 600
p = ttk.Progressbar(
    top_win,
    orient="horizontal",
    length=prog_total,
    mode="determinate",
    maximum=prog_total
)
#p['value'] = prog_total / 20,

p.pack()

'''
cursor	鼠标位于进度条内时的形状
length	进度条长度
maximum	进度条最大刻度值
mode 	进度条的模式。有两种：‘determinate’和’indeterminate’
orient	进度条的方向，有HORIZONTAL 和VERTICAL两种
style	定义进度条的外观
takefocus	是否可以通过Tab获得输入焦点
variable	与进度条关联的变量。可以设置或获得进度条的当前值
value	设置或者获取进度条的当前值
'''


def prog_start():
    p.start()
    return
def prog_stop():
    p.stop()
    return


prog_current = 0
def prog_set():
    global prog_current
    prog_current += 10
    p['value'] = prog_current
    return


btn_start_auto = tk.Button(top_win, text="Auto start progress", command=prog_start)
btn_start_auto.pack()
btn_stop = tk.Button(top_win, text="Stop progress", command=prog_stop)
btn_stop.pack()

btn_start_manual = tk.Button(top_win, text="Manual start progress", command=prog_set)
btn_start_manual.pack()


# show window and get into event loop
top_win.mainloop()
