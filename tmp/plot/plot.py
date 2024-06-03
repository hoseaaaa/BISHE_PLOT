import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse
import sys
import re
def plot_csr(filename, output_filename):
    # 检查命令行参数是否包含文件名

    # 获取文件名

    # 打开文件
    with open(filename, 'r') as file:
        # 读取文件内容并按行分割
        lines = file.readlines()

    # 使用正则表达式提取括号内的数字，并将每行的数组分割并存储到相应的变量中
    a = [int(num) for num in re.findall(r'\d+', lines[0])]
    # 使用空格分割数字，并将每行的数组分割并存储到相应的变量中
    indptr = [int(num) for num in lines[1].strip().split()]
    indices = [int(num) for num in lines[2].strip().split()]
    data = [float(num) for num in lines[3].strip().split()]


    # 假设你有一个CSR格式的稀疏矩阵
    # data = [10,20,30,40,50,60,70,80]
    # indices = [0,1,1,3,2,3,4,5]
    # indptr = [0,2,4,7,8]

    # 创建稀疏矩阵
    csr_matrix = scipy.sparse.csr_matrix((data, indices, indptr), shape=(a[0], a[1]))

    # 将稀疏矩阵转换为密集矩阵（Dense Matrix）
    dense_matrix = csr_matrix.toarray()

    # 绘制密集矩阵
    plt.imshow(dense_matrix, cmap='coolwarm', interpolation='nearest')

    # 显示行和列的刻度
    plt.xticks(np.arange(dense_matrix.shape[1]))
    plt.yticks(np.arange(dense_matrix.shape[0]))

    # 显示颜色条
    plt.colorbar()
    # 保存图形
    plt.savefig(output_filename)
    # 显示图形
    # plt.show()


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py input_filename output_filename")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    plot_csr(input_filename, output_filename)