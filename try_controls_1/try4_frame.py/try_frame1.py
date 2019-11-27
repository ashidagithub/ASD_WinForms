# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Frame )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
'''
加载背景图片需要使用 PIL
pip install pillow
'''
from PIL import Image, ImageTk

# tk._test()  # 测试 tkinter 是否正常工作

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
top_win.geometry(win_size_pos)

#框架布局
frame_root = tk.Frame(top_win)
frame_l = tk.Frame(frame_root)
frame_r = tk.Frame(frame_root)
#创建一个标签，并在窗口上显示
tk.Label(frame_l, text="中国", bg="red", font=("Arial", 12), width=10, height=2).pack(side='top')
tk.Label(frame_l, text="日本", bg="white", font=("Arial", 12), width=10, height=2).pack(side='top')
tk.Label(frame_r, text="美国", bg="blue", font=("Arial", 12), width=10, height=2).pack(side='top')
tk.Label(frame_r, text="韩国", bg="green", font=("Arial", 12), width=10, height=2).pack(side='top')
#框架的位置布局
frame_l.pack(side='left')
frame_r.pack(side='right')
frame_root.pack()




# show window and get into event loop
top_win.mainloop()
