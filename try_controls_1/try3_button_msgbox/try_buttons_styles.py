# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( button, messagebox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from PIL import Image, ImageTk

# create top_win window
top_win = tk.Tk()

# naming top_win window
top_win.title('Hello World Window')

# resize root window
top_win.geometry('800x600')

# 没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。
# 你可能在开发一个应用程序的时候想实现这种按钮，比如为了不干扰你的beta版的测试者：
btn_help = tk.Button(top_win, text="Help", command=None)
btn_help.pack()

button_relieves = ('flat', 'groove', 'raised', 'ridge', 'solid', 'sunken')

# 按钮样式 与前景背景色
for r in button_relieves:
    tk.Button(top_win, text=r, relief=r, fg='white', bg='blue').pack()

# 按钮边框
for b in [0, 1, 2, 3, 4]:
    text = 'Button border = %d' % b
    tk.Button(top_win, text=text, bd=b).pack()

# 状态
for st in ['norma', 'active', 'disabled']:
    tk.Button(top_win, text=st, state=st).pack()

# 图片按钮
image = Image.open(r'btn1_shutdown.jpg')
bk_img = ImageTk.PhotoImage(image)
tk.Button(top_win, text='try pic', compound='center', image=bk_img).pack()

# show window and waiting for event
top_win.mainloop()
