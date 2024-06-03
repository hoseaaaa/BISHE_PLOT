#!/usr/bin/env python
from pylab import *
from scipy.io import mmread
from scipy.sparse import csr_matrix
from scipy.sparse import random
import sys
import scipy.sparse
import re
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

fig, (ax1, ax2) = subplots(2, 1, sharex=True, figsize=(8, 10), gridspec_kw=dict(height_ratios=[4, 1]))
ax1.spy(A, marker='.', markersize=0.6, alpha=0.6)
ax2.semilogy(A.diagonal())
ax2.set_ylabel('Diagonal')
tight_layout()

savefig(output_filename)