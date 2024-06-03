import numpy as np
import sys
import re
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import norm, svds, LinearOperator
from scipy.linalg import lstsq
from scipy.sparse.linalg import cg, spsolve, LinearOperator

def sparse_matrix_condition_number_cg_preconditioned(A, tol=1e-6, maxiter=None):
    # Using a sparse matrix representation
    A_sparse = csr_matrix(A)

    # Using sparse matrix vector multiplication
    A_operator = LinearOperator(A_sparse.shape, matvec=lambda x: A_sparse.dot(x), rmatvec=lambda x: A_sparse.dot(x))

    # Solving linear system with sparse solver
    b = np.ones(A_sparse.shape[0])
    x, info = cg(A_operator, b, tol=tol, maxiter=maxiter)

    # Calculating relative residual
    relative_residual = np.linalg.norm(A_sparse.dot(x) - b) / np.linalg.norm(b)

    # Condition number estimate: 1 / (1 - relative residual)
    condition_number_estimate = 1 / (1 - relative_residual)

    return condition_number_estimate

# 创建一个稀疏矩阵的 CSR 格式
# data = np.array([1.0, 2.0, 3.0, 4.0, 5.0, 6.0])
# indices = np.array([0, 2, 2, 0, 1, 2])
# indptr = np.array([0, 2, 3, 6])
filename = sys.argv[1]
with open(filename, 'r') as file:
    # 读取文件内容并按行分割
    lines = file.readlines()
a = [int(num) for num in re.findall(r'\d+', lines[0])]
indptr = [int(num) for num in lines[1].strip().split()]
indices = [int(num) for num in lines[2].strip().split()]
data = [float(num) for num in lines[3].strip().split()]

A = csr_matrix((data, indices, indptr), shape=(a[0], a[1]))

# 计算条件数
condition_number = sparse_matrix_condition_number_cg_preconditioned(A)

print(f"The condition number of the sparse matrix is: {condition_number}")
