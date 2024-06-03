from compress import *
from csr_to_coo import *

def write_coo_to_file(csr, file_name):
    with open(file_name, 'w') as f:
        # 写入行数和列数
        rows, cols = csr.shape
        f.write("{} {}  ".format(rows, cols))
        
        # 写入非零元素总数
        f.write("{}\n".format(csr.nnz))
        
        # 写入indptr数组，每个元素之间用空格分隔
        f.write(" ".join(map(str, csr.indptr)) + "\n")
        
        # 写入indices数组，每个元素之间用空格分隔
        f.write(" ".join(map(str, csr.indices)) + "\n")
        
        # 写入data数组，每个元素之间用空格分隔
        f.write(" ".join(map(str, csr.data)) + "\n")

input_filename = sys.argv[1]
output_filename = sys.argv[2]

A=csr_to_coo(input_filename)
V,C=test_compression(A)

write_coo_to_file(C,output_filename),