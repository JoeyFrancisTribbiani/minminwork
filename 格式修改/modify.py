# -*- coding: GBK -*-
import csv
import os
import sys
import time

path = "."

resultfile = open("result.csv", 'a', encoding='gbk')
header = '"账号","中间值","date/time","settlement id","type","order id","sku","description","quantity","marketplace","account type","fulfillment","order city","order state","order postal","tax collection model","product sales","product sales tax","shipping credits","shipping credits tax","gift wrap credits","giftwrap credits tax","promotional rebates","promotional rebates tax","marketplace withheld tax","selling fees","fba fees","other transaction fees","other","total"\n'
resultfile.write(header)

account = sys.argv[1]
# account = "fuck"


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
