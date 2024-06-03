import matplotlib.pyplot as plt
import numpy as np

# 定义案例和数据
cases = ['ibmpg1', 'ibmpg2', 'ibmpg3', 'ibmpg4', 'ibmpg5', 'ibmpg6']
data = np.array([
    [16327, 4631, 740, np.nan],
    [126905, 28493, 3823, 256],
    [850626, 338099, 93626, 9568, 1473],
    [952618, 198732, 18102, 1008],
    [540220, 111029, 11396, 859],
    [834252, 185021, 20651, 1464]
], dtype=object)

# 定义横轴
x_axis = [0, 1, 2, 3, 4]

# 创建图表
plt.figure(figsize=(12, 8))

# 为每个案例绘制一条线
for idx, case_data in enumerate(data):
    # 计算当前案例数据的长度，并据此确定要使用的x轴数据
    current_length = len(case_data)
    current_x_axis = x_axis[:current_length]
    
    plt.plot(current_x_axis, case_data, marker='o', linestyle='-', label=cases[idx])

plt.title('')
plt.xlabel('Level')
plt.ylabel('Size')
plt.xticks(x_axis)  # 设置横轴刻度
plt.legend()
plt.grid(True)

plt.savefig('Corase_cross.png')
