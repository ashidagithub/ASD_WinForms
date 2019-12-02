# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Listbox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

'''
selectmode
判断多少项目可以选择,鼠标拖动如何影响选择:
BROWSE: 通常情况下,你只能选择一条线,一个ListBox。
如果您单击一个项目,然后拖动到不同的线路,选择将跟随鼠标。这是默认.
SINGLE: 你只能选择一条线,你可以拖不mouse.wherever的您单击按钮1,该行被选中.
MULTIPLE: 你可以选择任何的行数一次。点击任何行切换是否被选中.
EXTENDED: 你可以选择任何一次行相邻组的第一行上点击并拖动到最后一行.
'''
character = ("梅长苏","誉王","飞流","夏冬","霓凰郡主","蒙挚","萧景睿","谢玉")
lb_characters = tk.Listbox(top_win, selectmode=tk.EXTENDED)
for n in character:
    lb_characters.insert('end', n)
lb_characters.place(x=20, y=20, width=80, height=200)
# connect sb_character & lb_characters

players = ("胡歌","黄维德","吴磊","张龄心","刘涛","陈龙","程皓枫","刘奕君")
lb_players = tk.Listbox(top_win)
for n in players:
    lb_players.insert('end', n)
lb_players.place(x=160, y=20, width=80, height=200)

#设置第二个表格的项目颜色等
for i in range(len(players)):
    lb_players.itemconfig(i,fg="blue")
    if not i%2:
        lb_players.itemconfig(i,bg="#f0f0ff")

# ----------------------------------------
def show_msg(*args):
    #print('args=', args)
    indexs = lb_characters.curselection()
    if (len(indexs)>0):
        print('characters indexs=', indexs)
        player_index = indexs[0]
        lb_players.select_set(player_index)
    return


#为第一个Listbox设置绑定事件
lb_characters.bind("<<ListboxSelect>>",show_msg)


# show window and get into event loop
top_win.mainloop()
