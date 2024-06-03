import sys
import re

# 检查命令行参数是否包含文件名
if len(sys.argv) != 2:
    print("Usage: python script.py filename")
    sys.exit(1)

# 获取文件名
filename = sys.argv[1]

# 打开文件
with open(filename, 'r') as file:
    # 读取文件内容并按行分割
    lines = file.readlines()

# 使用正则表达式提取括号内的数字，并将每行的数组分割并存储到相应的变量中
a = [int(num) for num in re.findall(r'\d+', lines[0])]
b = [int(num) for num in lines[1].strip().split()]
c = [int(num) for num in lines[2].strip().split()]
d = [float(num) for num in lines[3].strip().split()]

# 打印结果
# print("a:", a[1])
# print("b:", b)
# print("c:", c)
d_sorted = sorted(d)
for num in d_sorted:
    print(num)
# print("d:", d)
