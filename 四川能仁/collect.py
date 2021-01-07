
import csv
import os

path = "."

resultfile = open("result.csv", 'a', encoding='utf-8')
header = '\"账号\",\"日期\",\"(父）ASIN\",\"（子）ASIN\",\"商品名称\",\"SKU\",\"买家访问次数\",\"买家访问次数百分比\",\"页面浏览次数\",\"页面浏览次数百分比\",\"购买按钮赢得率\",\"已订购商品数量\",\"订单商品数量转化率\",\"已订购商品销售额\",\"订单商品种类数\"\n'
resultfile.writelines(header)
# writer = csv.writer(resultfile)

# 遍历文件夹
# for file in files:
#     # 判断是否是文件夹，是文件夹才打开
#     if os.path.isdir(file) and not file.startswith('.'):
#         filelist = os.listdir(file)
#         for csvfile in filelist:
#             if (csvfile.startswith('.')):
#                 continue
#             # 读取csv至字典
#             f = open(path+"/"+file+"/"+csvfile, 'r',
#                      encoding='utf-8', errors='backslashreplace')
#             reader = csv.reader(f)

#             # 建立空字典
#             header = []
#             #reader = csv.DictReader(f)
#             reader = csv.reader((l.replace('\0', '') for l in f))

#             for item in reader:
#                 if reader.line_num != 1:
#                     break
#                 header.append("账号")
#                 header.append("日期")
#                 header.extend(item)

#             f.close()
#             writer.writerow(header)
#             headerflag = 1
#             break
#     if headerflag == 1:
#         break

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
