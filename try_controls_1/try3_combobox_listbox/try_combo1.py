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
#win_size_pos = '360x60'
top_win.geometry(win_size_pos)

# -------------------------------------


def func_comb_selected(event):
    'combox 选择数据后，自动执行的函数'
    sn = combo_op.current()
    info = combo_op.get()
    lbl_info['text'] = 'Selected No.(%d), value is %s' % (sn, info)
    return
# -------------------------------------


lbl_num1 = tk.Label(top_win, text='N1')
lbl_num1.place(x=20, y=20, anchor='nw')

entry_num1 = tk.Entry(top_win)
entry_num1.place(x=40, y=20, width=40, height=20)

lbl_num2 = tk.Label(top_win, text='N2')
lbl_num2.place(x=160, y=20, anchor='nw')

entry_num2 = tk.Entry(top_win)
entry_num2.place(x=180, y=20, width=40, height=20)

# 创建一个结果框
lbl_result = tk.Label(top_win,  text='result')
lbl_result.place(x=320, y=20,width=40, height=20, anchor='nw')

# 创建一个下拉列表
#combo_op = ttk.Combobox(top_win, width=12, textvariable=number)
combo_op = ttk.Combobox(top_win, width=4, state='readonly')
combo_op['values'] = ('＋', '－', '×', '÷')     # 设置下拉列表的值
combo_op.place(x=100, y=20)
combo_op.current(0)    # 设置下拉列表默认显示的值，0为 combo_op['values'] 的下标值
combo_op.bind("<<ComboboxSelected>>", func_comb_selected)

# 创建一个信息框
lbl_info = tk.Label(top_win, width=100, height=20, text='Please select...')
lbl_info.place(x=20, y=80, anchor='nw')

# 创建计算按钮及函数


def cmd_cal():
    '根据选择的运算符计算'
    num1 = int(entry_num1.get())
    num2 = int(entry_num2.get())
    operator = combo_op.get()
    if operator == '＋':
        result = num1 + num2
    elif operator == '－':
        result = num1 - num2
    elif operator == '×':
        result = num1 * num2
    elif operator == '÷':
        result = num1 / num2

    #print('result is %0.2f' % (result))
    lbl_result['text'] = '=%0.2f' % result

    return


btn_cal = tk.Button(top_win, text="Calculate", command=cmd_cal)
btn_cal.place(x=240, y=20, anchor='nw')

# show window and get into event loop
top_win.mainloop()
