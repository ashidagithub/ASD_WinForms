# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
'''
加载背景图片需要使用 PIL
pip install pillow
'''
from PIL import Image, ImageTk
import os

# tk._test()  # 测试 tkinter 是否正常工作

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
top_win.geometry(win_size_pos)

fpath = os.getcwd()
fpath += '\\try_controls_1\\try1_window\\mybk.jpg'
print(fpath)

# image = Image.open(r'mybk.jpg')
image = Image.open(fpath)
bk_img = ImageTk.PhotoImage(image)
# print(bk_img)
window_w = bk_img.width()
window_h = bk_img.height()
screen_w = top_win.winfo_screenwidth()
screen_h = top_win.winfo_screenheight()
# CENTER screen
x = (screen_w - window_w) / 2
y = (screen_h - window_h) / 2
# 注意参数类型是字符串。是 w*h+/-x+/-y的格式。
# x和y是位置（一般是窗口相对屏幕的坐标）
win_size_pos = "%dx%d+%d+%d" % (window_w, window_h, x, y)
# 放置背景图片
lbl_bk = tk.Label(top_win, image=bk_img)
lbl_bk.place(x=0, y=0, relwidth=1, relheight=1)
'''
'''

# show window and get into event loop
top_win.mainloop()
