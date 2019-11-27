# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Entry, Text )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk


# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
top_win.geometry('800x600')

# Try 1： Entry是tkinter类中提供的的一个单行文本输入域，
# 用来输入显示一行文本，收集键盘输入(类似 HTML 中的 text)

# 第4步，在图形界面上设定输入框控件entry并放置控件
txt_info = 'Hello world'
entry_cleartext = tk.Entry(top_win, show=None, font=('Arial', 14))  # 显示成明文形式
entry_cleartext.pack()
entry_cleartext.insert('insert',txt_info)

entry_ciphertext = tk.Entry(top_win, show='*', font=('Arial', 14))   # 显示成密文形式
entry_ciphertext.pack()
entry_ciphertext.insert('insert',txt_info)

# Try 2: Text是tkinter类中提供的的一个多行文本区域，显示多行文本，
# 可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，格式化文本显示，
# 允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
# 注意此处 height 为字符数，不是 pixel
text_description = tk.Text(top_win, height=6)
text_description.pack()

# Try 3: 为 text 填入文本
txt_info = 'Row1-xxxxxxx\nRow2-xxxxxxx\nRow3-xxxxxxx'
text_description.insert ('insert',txt_info)


# show window and get into event loop
top_win.mainloop()
