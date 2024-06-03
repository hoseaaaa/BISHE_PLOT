def f(x1, x2):
    """目标函数."""
    return x1**2 + x2**2

def df(x1, x2):
    """目标函数的梯度."""
    dfx1 = 2*x1  # 对x1的偏导
    dfx2 = 2*x2  # 对x2的偏导
    return dfx1, dfx2

def gradient_descent(x1_init, x2_init, learning_rate, max_iterations, tolerance):
    """梯度下降算法."""
    x1, x2 = x1_init, x2_init  # 初始化
    for i in range(max_iterations):
        dfx1, dfx2 = df(x1, x2)  # 计算梯度
        
        # 更新变量
        x1_new = x1 - learning_rate * dfx1
        x2_new = x2 - learning_rate * dfx2
        
        # 检查变化是否小于容忍度，如果是，则停止
        if abs(x1_new - x1) < tolerance and abs(x2_new - x2) < tolerance:
            break
        
        # 更新变量
        x1, x2 = x1_new, x2_new
    
    return x1, x2, i+1  # 返回最终的x1, x2和迭代次数

# 参数设置
x1_init, x2_init = 0.1, 0.1  # 初始值
learning_rate = 0.1  # 学习率
max_iterations = 1000  # 最大迭代次数
tolerance = 1e-6  # 容忍度

# 执行梯度下降
x1_min, x2_min, iters = gradient_descent(x1_init, x2_init, learning_rate, max_iterations, tolerance)

print(f"最小值在 x1={x1_min}, x2={x2_min}")
print(f"迭代次数: {iters}")
