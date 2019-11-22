# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window Class)
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox  # 这个是消息框，对话框的关键
import random


class AppUI:
    def __init__(self, top):
        '初始化类'
        self.root_win = top

        # 设置窗口大小、标题栏等基本信息
        self.root_win.title('Make window by class...')
        self.root_win.geometry('800x600')

        # 对窗口控件进行布局
        self.initWidgets()

        return

    def initWidgets(self):
        '对窗口内容进行布局'
        self.lbl_info = tk.Label(self.root_win, text='My label ', font=24)
        self.lbl_info.pack()
        self.btn_change = tk.Button(
            self.root_win, text='My button', command=self.change)
        self.btn_change.pack()
        return

    # 定义事件处理方法
    def change(self):
        '绑定事件，随机变换Label的背景色'
        # tk.messagebox.showinfo(title='Information', message='Show random RGB color for label') # 提示信息对话窗
        self.lbl_info['text'] = '欢迎学习Python'
        # 生成3个随机数，并凑成 RGB 模式
        ct = [random.randrange(256) for x in range(3)]
        # 计算该 RGB 色的灰度
        '''
　　    # 对于彩色转灰度，有一个很著名的心理学公式：
        # Gray = R*0.299 + G*0.587 + B*0.114
        '''
        #grayness = int(round(0.299 * ct[0] + 0.587 * ct[1] + 0.114 * ct[2]))
        grayness = (ct[0] * 299 + ct[1] * 587 + ct[2] * 114 + 500) / 1000
        # 将元组中3个随机数格式化成16进制数,转成颜色格式
        bg_color = "#%02x%02x%02x" % tuple(ct)
        # print(bg_color)
        self.lbl_info['bg'] = bg_color
        # 前景色默认为黑色，如果灰度大于 125 则变为白色
        if grayness > 125:
            self.lbl_info['fg'] = 'black'
        else:
            self.lbl_info['fg'] = 'white'
        return


if __name__ == '__main__':
    root = tk.Tk()
    AppUI(root)
    root.mainloop()
