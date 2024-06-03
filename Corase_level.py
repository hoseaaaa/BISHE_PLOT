import matplotlib.pyplot as plt

# 定义数据
cases = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']
rs_dim = [957, 1600, 1893, 2740, 2854, 2907]
sa_dim = [740, 256, 1473 , 1008, 859, 1464]
rs_non_zero = [8971, 21398, 13695, 40898, 38426, 36993]
sa_non_zero = [7934, 3510, 10873, 16152, 11755, 20886]

# 创建图表
fig, axs = plt.subplots(2, 1, figsize=(10, 10))

# 最粗层维度折线图
axs[0].plot(cases, rs_dim, marker='o', linestyle='-', color='blue', label='RS ')
axs[0].plot(cases, sa_dim, marker='s', linestyle='-', color='red', label='SA ')
axs[0].set_title('')
axs[0].set_xlabel('Cases')
axs[0].set_ylabel('Dimension')
axs[0].legend()
axs[0].grid(True)

# 最粗层非零元个数折线图
axs[1].plot(cases, rs_non_zero, marker='o', linestyle='-', color='blue', label='RS ')
axs[1].plot(cases, sa_non_zero, marker='s', linestyle='-', color='red', label='SA  ')
axs[1].set_title('')
axs[1].set_xlabel('Cases')
axs[1].set_ylabel('Non-Zero Elements')
axs[1].legend()
axs[1].grid(True)

# 显示图表
# 创建最粗层维度折线图并保存为图1
plt.figure(figsize=(8, 5))
plt.plot(cases, rs_dim, marker='o', linestyle='-', color='blue', label='RS ')
plt.plot(cases, sa_dim, marker='s', linestyle='-', color='red', label='SA ')
plt.title('')
plt.xlabel('Cases')
plt.ylabel('Dimension')
plt.legend()
plt.grid(True)
plt.savefig('Corase_Max_level.png')

# 创建最粗层非零元个数折线图并保存为图2
plt.figure(figsize=(8, 5))
plt.plot(cases, rs_non_zero, marker='o', linestyle='-', color='blue', label='RS ')
plt.plot(cases, sa_non_zero, marker='s', linestyle='-', color='red', label='SA ')
plt.title('')
plt.xlabel('Cases')
plt.ylabel('Non-Zero Elements')
plt.legend()
plt.grid(True)
plt.savefig('Corase_Max_nnz.png')
