# -*- coding: GBK -*-
import csv
import os
import sys
import time
from tkinter import *
import tkinter.filedialog
import tkinter as tk  # ʹ��Tkinterǰ��Ҫ�ȵ���

# ��1����ʵ����object����������window
window = tk.Tk()
path=''
resstr = tk.StringVar()    # ��label��ǩ����������Ϊ�ַ����ͣ���var������hit_me�����Ĵ�������������ʾ�ڱ�ǩ��

def start():
    global resstr
    os.chdir(path)

    #header = '"�˺�","�м�ֵ","date/time","settlement id","type","order id","sku","description","quantity","marketplace","account type","fulfillment","order city","order state","order postal","tax collection model","product sales","product sales tax","shipping credits","shipping credits tax","gift wrap credits","giftwrap credits tax","promotional rebates","promotional rebates tax","marketplace withheld tax","selling fees","fba fees","other transaction fees","other","total"\n'
    header = '"�˺�","return-date","order-id","sku","�м�ֵ","asin","fnsku","product-name","quantity","fulfillment-center-id","ԭ��","detailed-disposition","reason","status","license-plate-number","customer-comments"\n'

    defectivefile = open("defective.csv", 'w', encoding='gbk')
    defectivefile.writelines(header)

    dislikefile= open("dislike.csv", 'w', encoding='gbk')
    dislikefile.writelines(header)

    # account = sys.argv[1]
    account = '\"fuck\"'

    RETURN_DATE_COL = 0
    REASON_COL =11

    files = os.listdir(path)
    # �����ļ���
    for file in files:
        if not os.path.isdir(file) and file.endswith('.csv') and file!=('dislike.csv') and file!=('defective.csv'):
            f = open(path+"/"+file, 'r',
                     encoding='utf-8', errors='backslashreplace')
            line = f.readline()
            defective_row = ''
            dislike_row = ''
            while line:
                # ���Ե�һ��
                line = f.readline()
                if line == '':
                    continue

                arr = line.split('\",')
                for index,item in enumerate(arr[:-1]):
                    arr[index]= item+'\"'

                # datetime = arr[0][1:]+"," + ' '.join(arr[1].split(' ')[0:3])
                datestr = arr[0]
                # datestr = ' '.join(datetime)
                # bb = time.strptime(datestr, "%b %d, %Y %H:%M:%S")
                # cc = time.strftime("%Y%m%d", bb)
                datestr = datestr.split('T')[0]
                datearr = datestr.split('-')
                datestr = ''.join(datearr)
                arr[0] = datestr+'\"'
                # arr.remove(arr[1])

                arr.insert(0,account)
                arr.insert(4,'\"�м�ֵ\"')


                if arr[REASON_COL] == '\"DEFECTIVE\"':
                    arr.insert(10,'\"��������\"')
                    line = ','.join(arr)
                    defective_row = defective_row + line

                if arr[REASON_COL] != '\"DEFECTIVE\"':
                    arr.insert(10,'\"���˲�ϲ��\"')
                    line = ','.join(arr)
                    dislike_row = dislike_row + line

            f.close()
            defectivefile.writelines(defective_row)
            dislikefile.writelines(dislike_row)
    defectivefile.close()
    dislikefile.close()



# ��2���������ڵĿ��ӻ�������
window.title('���ݴ�����v1.0 - ����˻�����')
 
# ��3�����趨���ڵĴ�С(�� * ��)
window.geometry('500x300')  # ����ĳ���Сx
 
# ��4������ͼ�ν������趨��ǩ
var = tk.StringVar()    # ��label��ǩ����������Ϊ�ַ����ͣ���var������hit_me�����Ĵ�������������ʾ�ڱ�ǩ��
# ����һ���������ܣ������Լ����ɱ�д���������Button����ʱ���ã������������command=������
on_hit = False
def hit_me():
    global on_hit
    global path
    if on_hit == False:
        on_hit = True
        path=tkinter.filedialog.askdirectory()
        var.set('��ѡ��Ŀ¼��'+path)
        # var.set('dfdafdaa')
    else:
        on_hit = False
        var.set('')
 
# ��5�����ڴ��ڽ������÷���Button����
b = tk.Button(window, text='��˰�ťѡ����������Ŀ¼', font=('Arial', 12), width=10, height=5, command=hit_me)
b.pack(fill=X,padx=20,pady=10)

l = tk.Label(window, textvariable=var, bg='gray', fg='white', font=('Arial', 12), width=30, height=2)
# ˵���� bgΪ������fgΪ������ɫ��fontΪ���壬widthΪ����heightΪ�ߣ�����ĳ��͸����ַ��ĳ��͸ߣ�����height=2,���Ǳ�ǩ��2���ַ���ô��
l.pack(fill=X,padx=20,pady=10)

# ��5�����ڴ��ڽ������÷���Button����
w = tk.Button(window, text='��˰�ť��ʼ��������', font=('Arial', 12), width=30, height=5, command=start)
w.pack(fill=X,padx=20,pady=10)
 
r = tk.Label(window, textvariable=resstr, bg='gray', fg='white', font=('Arial', 12), width=30, height=2)
# ˵���� bgΪ������fgΪ������ɫ��fontΪ���壬widthΪ����heightΪ�ߣ�����ĳ��͸����ַ��ĳ��͸ߣ�����height=2,���Ǳ�ǩ��2���ַ���ô��
r.pack(fill=X,padx=20,pady=10)

# ��6����������ѭ����ʾ
window.mainloop()