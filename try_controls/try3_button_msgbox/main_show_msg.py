# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( button, messagebox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
import tkinter.messagebox #这个是消息框，对话框的关键

def cmd_print():
    print('Show in command window...')
    return

def cmd_pop():
    tk.messagebox.showinfo(title='Information', message='Normal Information') # 提示信息对话窗
    tk.messagebox.showwarning(title='Warning', message='Warning Information')  # 提出警告对话窗
    tk.messagebox.showerror(title='Error', message='Error Information')  # 提出错误对话窗
    return

# create top_win window
top_win = tk.Tk()

# naming top_win window
top_win.title('None World Window')

# resize root window
top_win.geometry('800x600')

btn_print = tk.Button(top_win, text="Show a message in command window", command=cmd_print)
btn_print.pack()

'''
messageBox：消息框，用于显示你应用程序的消息框。其实这里的messageBox就是我们平时看到的弹窗。
我们首先需要定义一个触发功能，来触发这个弹窗，这里我们就放上以前学过的button按钮，
通过触发功能，调用messagebox，点击button按钮就会弹出提示对话框
'''
btn_popup = tk.Button(top_win, text="Popup a message box", command=cmd_pop)
btn_popup.pack()


# show window and waiting for event
top_win.mainloop()
