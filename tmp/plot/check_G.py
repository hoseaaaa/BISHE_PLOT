import numpy as np
import sys
import re
import scipy.sparse
from scipy.linalg import cho_factor, cholesky
from scipy.sparse.linalg import eigsh
from scipy.linalg import LinAlgError

from scipy.sparse import csr_matrix
from scipy.linalg import cholesky
from scipy.linalg import cholesky
def is_symmetric(matrix):
    # Check if the matrix is symmetric
    return (matrix != matrix.T).nnz == 0


def is_positive_definite(matrix):
    # Check if the matrix is positive definite using eigsh to compute eigenvalues
    eigenvalues, _ = eigsh(matrix, k=1, which='SM')
    return eigenvalues[0] > 0

# def is_positive_definite(matrix):
#     try:
#         cholesky(matrix.toarray(), lower=True)
#         return True
#     except LinAlgError:
#         return False
# 获取文件名
filename = sys.argv[1]

# 打开文件
with open(filename, 'r') as file:
    # 读取文件内容并按行分割
    lines = file.readlines()

# 使用正则表达式提取括号内的数字，并将每行的数组分割并存储到相应的变量中
a = [int(num) for num in re.findall(r'\d+', lines[0])]
indptr = [int(num) for num in lines[1].strip().split()]
indices = [int(num) for num in lines[2].strip().split()]
data = [float(num) for num in lines[3].strip().split()]

# Example: Create a CSR matrix
# data = np.array([1.0, 2.0, 2.0, 3.0, 4.0])
# row_indices = np.array([0, 1, 1, 2, 2])
# col_indices = np.array([0, 1, 2, 1, 2])
matrix = scipy.sparse.csr_matrix((data, indices, indptr), shape=(a[0], a[1]))
# matrix = csr_matrix((data, (row_indices, col_indices)), shape=(a[0], a[1]))

# Check if the matrix is symmetric and positive definite
if is_symmetric(matrix) :
    print("The matrix is symmetric")
else:
    print("The matrix is not symmetric ")

if  is_positive_definite(matrix):
    print("The matrix is positive definite.")
else:
    print("The matrix is not positive definite.")
