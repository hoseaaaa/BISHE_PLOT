import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def generate_fine_grid(size):
    # 生成三维细网格
    x = np.linspace(0, 1, size)
    y = np.linspace(0, 1, size)
    z = np.linspace(0, 1, size)
    X, Y, Z = np.meshgrid(x, y, z)
    fine_grid = np.column_stack((X.ravel(), Y.ravel(), Z.ravel()))
    return fine_grid

def plot_grid(ax, grid, title):
    ax.plot_surface(grid[:, 0].reshape((int(np.sqrt(len(grid))), -1)),
                    grid[:, 1].reshape((int(np.sqrt(len(grid))), -1)),
                    grid[:, 2].reshape((int(np.sqrt(len(grid))), -1)),
                    cmap='viridis', edgecolor='k')
    ax.set_title(title)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_box_aspect([np.ptp(grid[:, 0]), np.ptp(grid[:, 1]), np.ptp(grid[:, 2])])

def algebraic_multigrid(coarse_size_factor, fine_size):
    fine_grid = generate_fine_grid(fine_size)
    
    # 复杂一点的粗化过程：每隔 coarse_size_factor 个点取一个点，并添加平均值
    coarse_grid = []
    for i in range(0, len(fine_grid), coarse_size_factor):
        if i + coarse_size_factor < len(fine_grid):
            average_point = np.mean(fine_grid[i:i+coarse_size_factor], axis=0)
            coarse_grid.append(average_point)
    coarse_grid = np.array(coarse_grid)
    
    return fine_grid, coarse_grid

def main():
    fine_size = 32
    coarse_size_factor = 4
    
    fine_grid, coarse_grid = algebraic_multigrid(coarse_size_factor, fine_size)
    
    fig = plt.figure(figsize=(12, 6))
    
    ax1 = fig.add_subplot(121, projection='3d')
    plot_grid(ax1, fine_grid, 'Fine Grid')

    ax2 = fig.add_subplot(122, projection='3d')
    plot_grid(ax2, coarse_grid, 'Coarse Grid (AMG)')

    plt.tight_layout()
    plt.show()

    plt.savefig("tmp.png")

if __name__ == "__main__":
    main()
