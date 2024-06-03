#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
from scipy.sparse import csr_matrix
import sys
import scipy.sparse
import re
from matplotlib.ticker import ScalarFormatter

# Set the font size
size = 20

# 读取矩阵数据并转换为CSR格式
input_filename = sys.argv[1]
output_filename = sys.argv[2]

with open(input_filename, 'r') as file:
    # 读取文件内容并按行分割
    lines = file.readlines()

# 使用正则表达式提取括号内的数字，并将每行的数组分割并存储到相应的变量中
a = [int(num) for num in re.findall(r'\d+', lines[0])]
# 使用空格分割数字，并将每行的数组分割并存储到相应的变量中
indptr = [float(num) for num in lines[1].strip().split()]
indices = [float(num) for num in lines[2].strip().split()]
data = [float(num) for num in lines[3].strip().split()]
A = scipy.sparse.csr_matrix((data, indices, indptr), shape=(a[0], a[1]))

fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True, figsize=(8, 10), gridspec_kw=dict(height_ratios=[4, 1]))

# Adjusting the plot for scientific notation
ax1.spy(A, marker='.', markersize=1.0, alpha=0.1)
ax2.semilogy(A.diagonal())

# Set font sizes for axis labels, tick labels, and titles
ax1.tick_params(axis='both', which='major', labelsize=size)
ax2.tick_params(axis='both', which='major', labelsize=size)
ax2.set_ylabel('Diagonal', fontsize=size)
ax1.set_title('Sparse Matrix Visualization', fontsize=size)

# Use scientific notation for y-axis in semilogy
formatter = ScalarFormatter(useMathText=True)
formatter.set_scientific(True)
formatter.set_powerlimits((-3, 3))

ax1.yaxis.set_major_formatter(formatter)
ax2.yaxis.set_major_formatter(formatter)

plt.tight_layout()
plt.savefig(output_filename)
plt.show()
