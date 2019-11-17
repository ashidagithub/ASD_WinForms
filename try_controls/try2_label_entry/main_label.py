# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Window )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk


# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
top_win.geometry('800x600')

# Try 1: Label：显示一个文本或图象。
# 在图形界面上设定标签
lbl_hello = tk.Label(top_win, text='Hello World!', bg='blue',
                     font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，font为字体，width为长，height为高，
# 这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高

# 用 pack() 放置标签
lbl_hello.pack()    # Label内容content区域放置位置，自动调节尺寸
# 放置lable的方法有：1）l.pack(); 2)l.place();

# 用 place() 放置 label
# 给精确的坐标来定位，如此处给的(50, 100)，就是将这个部件放在坐标为(x=50, y=100)的位置,
# 后面的参数 anchor='nw'，就是前面所讲的锚定点是西北角。
lbl_programmer = tk.Label(
    top_win, text='I am a programmer!', font=('Arial', 20), )
lbl_programmer.place(x=50, y=100, anchor='nw')

# Try 2: Text是tkinter类中提供的的一个多行文本区域，显示多行文本，
# 可用来收集(或显示)用户输入的文字(类似 HTML 中的 textarea)，格式化文本显示，
# 允许你用不同的样式和属性来显示和编辑文本，同时支持内嵌图象和窗口。
text_description = tk.Text(top_win, height=3)
text_description.pack()



# show window and waiting for event
top_win.mainloop()
