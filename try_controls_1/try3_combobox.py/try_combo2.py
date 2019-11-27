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


# 准备下拉框内的数据
data_province = ('安徽省', '江苏省', '浙江省')
city_AH = ('合肥市', '芜湖市', '蚌埠市', '淮南市', '马鞍山市', '淮北市', '铜陵市', '安庆市',
           '黄山市', '滁州市', '阜阳市', '宿州市', '巢湖市', '六安市', '亳州市', '池州市', '宣城市')
city_JS = ('南京市', '无锡市', '徐州市', '常州市', '苏州市', '南通市',
           '连云港市', '淮安市', '盐城市', '扬州市', '镇江市', '泰州市', '宿迁市')
city_ZJ = ('杭州市', '宁波市', '温州市', '嘉兴市', '湖州市',
           '绍兴市', '金华市', '衢州市', '舟山市', '台州市', '丽水市')
data_cities = (city_AH, city_JS, city_ZJ)

# -------------------------------------
def func_comb1_selected(event):
    '主从 combo 联动函数'
    sn = combo_province.current()
    # print(sn)
    combo_city['values'] = data_cities[sn]
    combo_city.current(0)
    refresh_lbl()
    return


def func_comb2_selected(event):
    refresh_lbl()
    return


def refresh_lbl():
    p = combo_province.get()
    c = combo_city.get()
    lbl_info['text'] = '地址：%s %s' % (p, c)
    return
# -------------------------------------


# 创建第一个下拉列表 - 省
combo_province = ttk.Combobox(top_win, width=20, state='readonly')
combo_province['values'] = data_province     # 设置下拉列表的值
combo_province.place(x=40, y=40)
combo_province.current(0)    # 设置下拉列表默认显示的值，0为 combo_province['values'] 的下标值
combo_province.bind("<<ComboboxSelected>>", func_comb1_selected)

# 创建第一个下拉列表 - 市
combo_city = ttk.Combobox(top_win, width=20, state='readonly')
combo_city['values'] = data_cities[0]     # 设置下拉列表的值
combo_city.place(x=220, y=40)
combo_city.current(0)    # 设置下拉列表默认显示的值，0为 combo_city['values'] 的下标值
combo_city.bind("<<ComboboxSelected>>", func_comb2_selected)

# 创建一个信息框
lbl_info = tk.Label(top_win, width=280, height=20,
                    anchor='nw', text='请选择省市...')
lbl_info.place(x=40, y=80)

# show window and get into event loop
top_win.mainloop()
