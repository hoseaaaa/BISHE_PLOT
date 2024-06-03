#!/usr/bin/env python
from pylab import *
import sys
import scipy.sparse
import re
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize
# 读取矩阵数据并转换为CSR格式
input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r') as file:
    # 读取文件内容并按行分割
    lines = file.readlines()

# 使用正则表达式提取括号内的数字，并将每行的数组分割并存储到相应的变量中
a = [int(num) for num in re.findall(r'\d+', lines[0])]
# 将indptr转换为整数列表
indptr = [int(num) for num in lines[1].strip().split()]
indices = [int(num) for num in lines[2].strip().split()]
data = [float(num) for num in lines[3].strip().split()]
A = scipy.sparse.csr_matrix((data, indices, indptr), shape=(a[0], a[1]))




# 绘图设置
fig, ax = plt.subplots(figsize=(5, 5))  # 调整大小以匹配你的具体需求
ax.set_aspect('equal', 'box')
ax.invert_yaxis()  # Y轴反向，与矩阵的行对齐

# 遍历矩阵中的非零元素并绘制
rows, cols = A.nonzero()
# 使用一个colormap来根据数值显示颜色
cmap = plt.get_cmap('coolwarm')
colors = [cmap((val + 1) / 2) for val in A.data]  # 归一化到0-1范围内的颜色映射
alphas = [abs(val) for val in A.data]  # Alpha值与归一化后数值的绝对大小成正比

# 绘制散点图
sc = ax.scatter(cols, rows, c=colors, s=10, alpha=alphas, edgecolors='none')

# 添加色条，它代表归一化后数值的大小
sm = ScalarMappable(norm=Normalize(vmin=-1, vmax=1), cmap=cmap)
sm.set_array([])
cbar = plt.colorbar(sm, ax=ax)
cbar.set_label('Normalized Magnitude')

plt.tight_layout()
plt.savefig(output_filename)











# fig, ax = plt.subplots(figsize=(8, 8))  # 创建一个绘图对象
# # 使用imshow绘制矩阵A，选择一个colormap，比如'coolwarm'，它对正负值有良好的区分
# # 'extent'参数用于调整坐标轴的范围
# im = ax.imshow(A.toarray(), cmap='coolwarm', interpolation='nearest', extent=[0, a[1], 0, a[0]])

# # 添加颜色条以表示颜色与数值的对应关系
# fig.colorbar(im, ax=ax)

# ax.set_aspect('equal', 'box')
# ax.invert_yaxis()  # y轴方向与矩阵行的方向一致
# plt.tight_layout()
plt.savefig(output_filename)
