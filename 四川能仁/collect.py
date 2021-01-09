import csv
import os
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
    resultfile = open("result.csv", 'a', encoding='utf-8')
    header = '\"账号\",\"日期\",\"(父）ASIN\",\"（子）ASIN\",\"商品名称\",\"SKU\",\"买家访问次数\",\"买家访问次数百分比\",\"页面浏览次数\",\"页面浏览次数百分比\",\"购买按钮赢得率\",\"已订购商品数量\",\"订单商品数量转化率\",\"已订购商品销售额\",\"订单商品种类数\"\n'
    resultfile.writelines(header)

    files = os.listdir(path)
    # 遍历文件夹
    for file in files:
        # 判断是否是文件夹，是文件夹才打开
        if os.path.isdir(file) and not file.startswith('.'):
            filelist = os.listdir(file)
            for csvfile in filelist:
                if (csvfile.startswith('.')):
                    continue
                f = open(path+"/"+file+"/"+csvfile, 'r',
                         encoding='utf-8', errors='backslashreplace')
                # reader = csv.reader((l.replace('\0', '') for l in f))

                # 建立空字典
                # rlist=[]

                line = f.readline()
                row = ''
                i = 0
                while line:
                    # 忽略第一行
                    i = i + 1
                    if i == 1:
                        continue
                    line = f.readline()
                    if line == '':
                        continue
                    row = row + ('\"' + file +
                                 '\",') + ('\"' + csvfile.split('.')[0] + '\",') + line
                f.close()
                resultfile.writelines(row)

    resultfile.close()
    resstr.set('数据处理完成，处理结果保存在上面的目录，名字是result.csv')

 
# 第2步，给窗口的可视化起名字
window.title('数据处理工具v1.0')
 
# 第3步，设定窗口的大小(长 * 宽)
window.geometry('500x300')  # 这里的乘是小x
 
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
b = tk.Button(window, text='点此按钮选择数据所在目录',bg='black', font=('Arial', 12), width=10, height=5, command=hit_me)
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