import numpy as np
from scipy.sparse import csr_matrix, coo_matrix
from pylab import *
from scipy.io import mmread
from scipy.sparse import random
import sys
import scipy.sparse
import re


# Function to convert CSR to COO format

# Test routine
def csr_to_coo(input_filename):
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

    # Create a CSR-format sparse matrix for testing

    A_coo = A.tocoo()
    
    # # Print the COO representation
    # print("Values:", coo.data)
    # print("Row indices:", coo.row)
    # print("Column indices:", coo.col)
    return A_coo
