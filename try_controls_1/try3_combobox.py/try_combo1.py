# -*- coding: UTF-8 -*-

# ------------------------(max to 80 columns)-----------------------------------
# author by : （学员ID)
# created:  2019.11

# Description:
#   初步学习 WinForm 编程 ( Combobox )
# ------------------------(max to 80 columns)-----------------------------------

import tkinter as tk
from tkinter import ttk

# create root window
top_win = tk.Tk()

# naming root window
top_win.title('Hello World Window')

# resize root window
win_size_pos = '800x600'
top_win.geometry(win_size_pos)

# -------------------------------------
def func_comb_selected(event):
    'combox 选择数据后，自动执行的函数'
    sn = combo_test.current()
    info = combo_test.get()
    lbl_info['text'] = 'Selected No.(%d), value is %s' % (sn, info)
    return
# -------------------------------------


# 创建一个下拉列表
#combo_test = ttk.Combobox(top_win, width=12, textvariable=number)
combo_test = ttk.Combobox(top_win, width=12, state='readonly')
# combo_test['values'] = ('加','减', '乘','除')     # 设置下拉列表的值
combo_test['values'] = ('加','减', '乘','除')     # 设置下拉列表的值
combo_test.pack()
combo_test.current(0)    # 设置下拉列表默认显示的值，0为 combo_test['values'] 的下标值
combo_test.bind("<<ComboboxSelected>>", func_comb_selected)

# 创建一个信息框
lbl_info = tk.Label(top_win, width=100, height=20, text='Please select...')
lbl_info.pack()


# show window and get into event loop
top_win.mainloop()
