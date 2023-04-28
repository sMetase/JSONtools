'''
csv2json.py
简单的csv转换为json的脚本
sMetase
2023/04/28
'''

import csv
import json


# 默认保存位置在同一目录下
path = input("Please enter your file path.\n")
output_file = path.replace('csv', 'json')

# 读入csv文件
data = []
with open(path, 'r', encoding='utf-8') as f:
    for row in csv.DictReader(f):
        data.append(row)
f.close()


# 转换成json文件并写入
fw = open(output_file, "w", encoding='utf-8')
# 为保证中文的正常输出ensure_ascii应为False， 保证可读性则设置缩进为4
json_data = json.dumps(data, ensure_ascii=False, indent=4)
fw.write(json_data)
fw.close()
print("Done!")