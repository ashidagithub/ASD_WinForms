# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Label )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from PIL import Image, ImageTk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
top_win.geometry('800x600')

# Try 1: 用 lable 显示背景图片
image = Image.open(r'mybk.jpg')
bk_img = ImageTk.PhotoImage(image)
# 放置背景图片
lbl_bk = tk.Label(top_win, image=bk_img)
lbl_bk.place(x=0, y=0, relwidth=1, relheight=1)

# Try 2: Label：显示一个文本标签
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

# Try 3： 用Label 显示动图 gif
'''
image = Image.open('RPS_animation.gif')
animation_img = ImageTk.PhotoImage(image)
lbl_animation = tk.Label(top_win)
lbl_animation.configure(image=animation_img)
lbl_animation.image = animation_img
#lbl_animation.place(x=50, y=300, anchor='nw')
lbl_animation.pack()

frames = [ImageTk.PhotoImage(file='RPS_animation.gif',format = 'gif -index %i' %(i)) for i in range(3)]
print(frames[0])
print(frames[1])
print(frames[2])
def update(ind):
    if ind>=3:
        ind = 0
    frame = frames[ind]
    #print(ind)
    ind += 1
    lbl_animation.configure(image=frame)
    top_win.after(3, update, ind)
lbl_animation = tk.Label(top_win)
lbl_animation.pack()
top_win.after(3, update, 0)
'''
# show window and get into event loop
top_win.mainloop()
