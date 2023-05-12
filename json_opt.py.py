'''
json_opt.py
sMetase
2024/05/12

a simple tool for improving the readability
of JSON files
'''
import os
import json

# 获取当前文件地址
curr_dir = os.path.dirname(os.path.abspath(__file__))

# 遍历当前文件夹
for filename in os.listdir(curr_dir):

    # 确定是JSON文件
    if filename.endswith('.json'):
        file_path = os.path.join(curr_dir, filename)
        # 加载JSON文件
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # 优化可读性
        new_data = json.dumps(data, ensure_ascii=False, indent=4)
        # 生成修改后的文件名称
        file_basename = os.path.splitext(file_path)[0]
        file_ext = os.path.splitext(file_path)[1]
        new_file_base_name = file_basename + '_processed'
        new_path = os.path.join(curr_dir, new_file_base_name + file_ext)

        # 生成新文件
        with open(new_path, 'w', encoding='utf-8') as fn:
            fn.write(new_data)

print('Done!')