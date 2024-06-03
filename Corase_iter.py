import matplotlib.pyplot as plt

# 定义数据
cases = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']
rs_dim = [22,22,26,28,28,26]
sa_dim = [16,14,17,18,15,18]

# 创建图表
fig, axs = plt.subplots(2, 1, figsize=(10, 10))





# 显示图表
# 创建最粗层维度折线图并保存为图1
plt.figure(figsize=(8, 5))
plt.plot(cases, rs_dim, marker='o', linestyle='-', color='blue', label='RS ')
plt.plot(cases, sa_dim, marker='s', linestyle='-', color='red', label='SA ')
plt.title('')
plt.xlabel('Cases')
plt.ylabel('Iters')
plt.legend()
plt.grid(True)
plt.savefig('Corase_Max_iter.png')

