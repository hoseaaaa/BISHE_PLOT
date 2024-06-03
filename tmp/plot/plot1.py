import matplotlib.pyplot as plt
from scipy.sparse import csr_matrix
import numpy as np

# 创建一个CSR格式的稀疏矩阵
data = np.array([1, 2, 3, 4, 5, 6])
row_indices = np.array([0, 0, 1, 2, 2, 3])
col_indices = np.array([1, 2, 2, 0, 1, 3])
sparse_matrix = csr_matrix((data, (row_indices, col_indices)), shape=(4, 4))

# 获取非零元素的行、列坐标
nonzero_rows, nonzero_cols = sparse_matrix.nonzero()

# 可视化稀疏矩阵结构
plt.figure(figsize=(8, 8))
plt.scatter(nonzero_cols, nonzero_rows, marker='s', c='blue', s=100)
plt.title('Sparse Matrix Structure (CSR Format)')
plt.xlabel('Column Index')
plt.ylabel('Row Index')
plt.grid(True)

# 保存图片到文件
plt.savefig('sparse_matrix_structure_csr.png')

# 显示图形（可选）
plt.show()
