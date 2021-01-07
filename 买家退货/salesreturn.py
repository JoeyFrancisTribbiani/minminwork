# -*- coding: GBK -*-
import csv
import os
import sys
import time

path = "."

#header = '"账号","中间值","date/time","settlement id","type","order id","sku","description","quantity","marketplace","account type","fulfillment","order city","order state","order postal","tax collection model","product sales","product sales tax","shipping credits","shipping credits tax","gift wrap credits","giftwrap credits tax","promotional rebates","promotional rebates tax","marketplace withheld tax","selling fees","fba fees","other transaction fees","other","total"\n'
header = '"账号","return-date","order-id","sku","中间值","asin","fnsku","product-name","quantity","fulfillment-center-id","原因","detailed-disposition","reason","status","license-plate-number","customer-comments"\n'

defectivefile = open("defective.csv", 'w', encoding='gbk')
defectivefile.writelines(header)

dislikefile= open("dislike.csv", 'w', encoding='gbk')
dislikefile.writelines(header)

# account = sys.argv[1]
account = '\"fuck\"'

RETURN_DATE_COL = 0
REASON_COL =11

files = os.listdir(path)
# 遍历文件夹
for file in files:
    if not os.path.isdir(file) and file.endswith('.csv') and file!=('dislike.csv') and file!=('defective.csv'):
        f = open(path+"/"+file, 'r',
                 encoding='utf-8', errors='backslashreplace')
        line = f.readline()
        defective_row = ''
        dislike_row = ''
        while line:
            # 忽略第一行
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
            arr.insert(4,'\"中间值\"')
            

            if arr[REASON_COL] == '\"DEFECTIVE\"':
                arr.insert(10,'\"质量问题\"')
                line = ','.join(arr)
                defective_row = defective_row + line

            if arr[REASON_COL] != '\"DEFECTIVE\"':
                arr.insert(10,'\"客人不喜欢\"')
                line = ','.join(arr)
                dislike_row = dislike_row + line

        f.close()
        defectivefile.writelines(defective_row)
        dislikefile.writelines(dislike_row)
defectivefile.close()
dislikefile.close()
