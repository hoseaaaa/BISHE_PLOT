import statsmodels.api as sm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# 假设从 'sita' 模块中导入的内容在这里不再需要
from statsmodels.nonparametric.smoothers_lowess import lowess
from sita import *

# 假设 'df' 是已经定义好的 DataFrame

# 添加常数项到独立变量中，以便在回归中包括截距
X = sm.add_constant(df['theta'])
y = df['normalized_levels']

# 执行回归
model = sm.OLS(y, X).fit()

# 获取回归结果概要，其中包含 p 值和 R 方等统计量
summary = model.summary()
print(summary)

# 提取 R 方值
r_squared = model.rsquared

# 生成 p 值的直方图
fig, ax = plt.subplots(figsize=(6, 5))
p_value = model.pvalues[1]  # theta 系数的 p 值
ax.hist([p_value], bins=10, color='blue', edgecolor='black')
ax.set_xscale('log')
ax.set_title('p-value')
ax.set_xlabel('pvalue')
ax.set_ylabel('density')
plt.tight_layout()
plt.savefig("Sita_p_value.png")  # 保存第一张图

# 生成 R 方的直方图
fig, ax = plt.subplots(figsize=(6, 5))
ax.hist([r_squared], bins=10, color='blue', edgecolor='black')
ax.set_title('R-squared')
ax.set_xlabel('R²')
ax.set_ylabel('density')
plt.tight_layout()
plt.savefig("Sita_r_squared.png")  # 保存第二张图

