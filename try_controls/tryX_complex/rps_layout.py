# -*- coding: UTF-8 -*-

'''
# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   利用已经学过的控件编制一个石头剪子布游戏
#   Rock,Paper,Scissors
# ------------------------(max to 80 columns)-----------------------------------
'''

import tkinter as tk
import random

import pkg_place_controls.main_win as main_win

# ----------------------------------------------------------
# Step 1: 创建主窗口
# create root window
top_win = tk.Tk()
# naming root window
top_win.title('Rock Paper Scissors Game')
# calculate root window's size and posiztion
win_size_pos = main_win.get_win_size_pos_standard(top_win)
# place root window
top_win.geometry(win_size_pos)

# ----------------------------------------------------------
# Step 2: 放置机器人头像
lbl_robot = tk.Label(top_win, text='Robot', bg='yellow')
lbl_robot.place(x=40, y=40, width=140, height=200)

# ----------------------------------------------------------
# Step 3: 放置挑战者信息
lbl_player = tk.Label(top_win, text='Please input player''s name ', bg='white')
lbl_player.place(x=220, y=40, width=160, height=20)

entry_player_name = tk.Entry(top_win, show=None)
entry_player_name.place(x=220, y=60, width=160, height=20)

# ----------------------------------------------------------
# Step 4: 放置4个进度条的 Label
lbl_prog = []

lbl_progress0 = tk.Label(top_win, text='Ready', bg='gray')
lbl_prog.append(lbl_progress0)
lbl_progress1 = tk.Label(top_win, text='1 s', bg='gray')
lbl_prog.append(lbl_progress1)
lbl_progress2 = tk.Label(top_win, text='2 s', bg='gray')
lbl_prog.append(lbl_progress2)
lbl_progress3 = tk.Label(top_win, text='3 s', bg='gray')
lbl_prog.append(lbl_progress3)
for idx in range(4):
    pos_x = 220 + idx * 40
    pos_y = 100
    lbl_prog[idx].place(x=pos_x, y=pos_y, width=40, height=60)

# ----------------------------------------------------------
# Step 5: 放置本场比赛信息框、得分框
lbl_current_race_info = tk.Label(
    top_win, text='Current Race Info', bg='orange')
lbl_current_race_info.place(x=220, y=180, width=100, height=60)

lbl_current_score_title = tk.Label(top_win, text='Score', bg='orange')
lbl_current_score_title.place(x=340, y=180, width=40, height=20)

lbl_current_score = tk.Label(top_win, text='5', bg='red', fg='white')
lbl_current_score.place(x=340, y=200, width=40, height=40)

# ----------------------------------------------------------
# Step 6: 放置历届比赛信息框、得分框
lbl_history_race_title = tk.Label(top_win, text='History Score List', bg='gray')
lbl_history_race_title.place(x=40, y=260, width=340, height=40)

lbl_history_race = []
for idx in range(13):
    score_name = tk.Label(top_win, text='Score=XX  Player is xxxxxxxx', bg='white')
    score_name.place(x=40, y=(300+idx*20), width=200, height=20)

    score_detail = tk.Label(top_win, text='Vict=XX Draw=XX Lose=XX', bg='white')
    score_detail.place(x=240, y=(300+idx*20), width=140, height=20)

    score_info = (score_name, score_detail)
    lbl_history_race.append(score_info)

# ----------------------------------------------------------
# Step 7: 放置比赛开始按钮
btn_start = tk.Button(top_win, text="Start Game", bg='green', command=None)
btn_start.place(x=420, y=40, width=140, height=40)

# ----------------------------------------------------------
# Step 8: 放置石头剪子布按钮
btn_rock = tk.Button(top_win, text="Rock", bg='white', command=None)
btn_rock.place(x=420, y=100, width=140, height=140)

btn_paper = tk.Button(top_win, text="Paper", bg='white', command=None)
btn_paper.place(x=420, y=260, width=140, height=140)

btn_scissors = tk.Button(top_win, text="Scissors", bg='white', command=None)
btn_scissors.place(x=420, y=420, width=140, height=140)

# Step FINAL
# 进入消息循环
top_win.mainloop()
