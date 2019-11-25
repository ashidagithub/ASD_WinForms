# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( button, messagebox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
import tkinter.messagebox  # 这个是消息框，对话框的关键
from PIL import Image, ImageTk


def cmd_pop():
    tk.messagebox.showinfo(title='Information',
                           message='Mouse clicked !')  # 提示信息对话窗
    return


def e_btn(event):
    tk.messagebox.showinfo(title='Information',
                           message='Enter pressed !')  # 提示信息对话窗
    return


# create top_win window
top_win = tk.Tk()

# naming top_win window
top_win.title('Hello World Window')

# resize root window
top_win.geometry('800x600')

# 没有回调函数的按钮是没有用的，当你按下这个按钮时它什么也不做。
# 你可能在开发一个应用程序的时候想实现这种按钮，比如为了不干扰你的beta版的测试者：
btn_help = tk.Button(top_win, text="Enter", command=cmd_pop)
btn_help.bind('<Return>', e_btn)
btn_help.focus_set()
btn_help.pack()


# show window and waiting for event
top_win.mainloop()
