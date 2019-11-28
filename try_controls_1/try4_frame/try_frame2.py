# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( LabelFrame )
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


# Step1: Create frame
frame_root1 = tk.Frame(top_win, bg="grey", width=760, height=200)
# frame_root1.pack()
frame_root1.place(x=20, y=20)


# Step2: Appedn other controls
lbl_test = tk.Label(frame_root1, text='text in frame')
lbl_test.place(x=20, y=60)


# Step3: Create Label Frame
frame_root2 = tk.LabelFrame(top_win, bg="grey", width=760, height=200, text='My Frame')
# frame_root1.pack()
frame_root2.place(x=20, y=240)


# Step4: Appedn other controls
lbl_test = tk.Label(frame_root2, text='text in label frame')
lbl_test.place(x=20, y=60)




# show window and get into event loop
top_win.mainloop()
