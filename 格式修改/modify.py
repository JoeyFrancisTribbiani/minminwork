# -*- coding: GBK -*-
import csv
import os
import sys
import time
from tkinter import *
import tkinter.filedialog
import tkinter as tk  # 使用Tkinter前需要先导入

# 第1步，实例化object，建立窗口window
window = tk.Tk()
path=''
resstr = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上

def start():
    global resstr
    os.chdir(path)
    resultfile = open("result.csv", 'a', encoding='gbk')
    header = '"账号","中间值","date/time","settlement id","type","order id","sku","description","quantity","marketplace","account type","fulfillment","order city","order state","order postal","tax collection model","product sales","product sales tax","shipping credits","shipping credits tax","gift wrap credits","giftwrap credits tax","promotional rebates","promotional rebates tax","marketplace withheld tax","selling fees","fba fees","other transaction fees","other","total"\n'
    resultfile.write(header)

    account = '默认账号名'

    files = os.listdir(path)
    # 遍历文件夹
    for file in files:
        if not os.path.isdir(file) and file.endswith('.csv') and file!=('result.csv'):
            f = open(path+"/"+file, 'r',
                     encoding='utf-8', errors='backslashreplace')
            line = f.readline()
            row = ''
            i = 0
            while line:
                # 忽略第一行
                i = i + 1
                line = f.readline()
                if i <= 7:
                    continue
                if line == '':
                    continue
                arr = line.split(',')
                if arr[3] != '\"Refund\"':
                    continue

                datetime = arr[0][1:]+"," + ' '.join(arr[1].split(' ')[0:3])
                datestr = datetime
                # datestr = ' '.join(datetime)
                bb = time.strptime(datestr, "%b %d, %Y %H:%M:%S")
                cc = time.strftime("%Y%m%d", bb)
                arr[0] = '\"'+cc+'\"'
                arr.remove(arr[1])

                total = arr[-1]
                if total.startswith('\"-'):
                    total = total[2:]
                    arr[-1] = total

                line = ','.join(arr)
                row = row + ('\"' + account +'\",') + ('\"midvalue\",') + line 
            f.close()
            resultfile.writelines(row)

    resultfile.close()
    resstr.set('数据处理完成，处理结果保存在上面的目录，名字是result.csv')

# 第2步，给窗口的可视化起名字
window.title('数据处理工具v1.0 - 格式修改')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x400')  # 这里的乘是小x
 
# 第4步，在图形界面上设定标签
var = tk.StringVar()    # 将label标签的内容设置为字符类型，用var来接收hit_me函数的传出内容用以显示在标签上
# 定义一个函数功能（内容自己自由编写），供点击Button按键时调用，调用命令参数command=函数名
on_hit = False
def hit_me():
    global on_hit
    global path
    if on_hit == False:
        on_hit = True
        path=tkinter.filedialog.askdirectory()
        var.set('已选择目录：'+path)
        # var.set('dfdafdaa')
    else:
        on_hit = False
        var.set('')
 
# 第5步，在窗口界面设置放置Button按键
b = tk.Button(window, text='点此按钮选择数据所在目录', font=('Arial', 12), width=10, height=5, command=hit_me)
b.pack(fill=X,padx=20,pady=10)

l = tk.Label(window, textvariable=var, bg='gray', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
l.pack(fill=X,padx=20,pady=10)

# 第5步，在窗口界面设置放置Button按键
w = tk.Button(window, text='点此按钮开始处理数据', font=('Arial', 12), width=30, height=5, command=start)
w.pack(fill=X,padx=20,pady=10)
 
r = tk.Label(window, textvariable=resstr, bg='gray', fg='white', font=('Arial', 12), width=30, height=2)
# 说明： bg为背景，fg为字体颜色，font为字体，width为长，height为高，这里的长和高是字符的长和高，比如height=2,就是标签有2个字符这么高
r.pack(fill=X,padx=20,pady=10)

# 第6步，主窗口循环显示
window.mainloop()