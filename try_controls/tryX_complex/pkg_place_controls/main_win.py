# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   计算并显示主窗口
# ------------------------(max to 80 columns)-----------------------------------


# ---------------------------------------------------
import sys
import os
from PIL import Image, ImageTk
# ---------------------------------------------------
sys.path.append('..')
# ---------------------------------------------------


def get_win_size_pos_standard(game_win):
    '按照设计书规定的尺寸返回窗口的大小及居中位置'

    window_w = 600
    window_h = 600
    screen_w = game_win.winfo_screenwidth()
    screen_h = game_win.winfo_screenheight()
    # CENTER screen
    x = (screen_w - window_w) / 2
    y = (screen_h - window_h) / 2
    # 注意参数类型是字符串。是 w*h+/-x+/-y的格式。
    # x和y是位置（一般是窗口相对屏幕的坐标）
    win_size_pos = "%dx%d+%d+%d" % (window_w, window_h, x, y)

    return win_size_pos


def get_win_size_pos_by_bkimg(game_win):
    '依据图片大小返回主窗口的大小及居中位置'

    img_path = os.getcwd() + '\\images\\title_img.jpg'
    image = Image.open(img_path)
    bk_img = ImageTk.PhotoImage(image)
    # print(bk_img)
    window_w = bk_img.width()
    window_h = bk_img.height()
    screen_w = game_win.winfo_screenwidth()
    screen_h = game_win.winfo_screenheight()
    # CENTER screen
    x = (screen_w - window_w) / 2
    y = (screen_h - window_h) / 2
    # 注意参数类型是字符串。是 w*h+/-x+/-y的格式。
    # x和y是位置（一般是窗口相对屏幕的坐标）
    win_size_pos = "%dx%d+%d+%d" % (window_w, window_h, x, y)
    return win_size_pos
