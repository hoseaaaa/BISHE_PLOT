import numpy as np
from scipy.sparse import coo_matrix, csr_matrix

def compression(Ah_coo, m, opt):
    val, row, col = Ah_coo.data, Ah_coo.row, Ah_coo.col
    n = Ah_coo.shape[0]
    V = np.zeros((m, m))
    C = np.zeros((m, m))
    B = np.zeros((m, m))


    q = n // m
    p = n % m
    t = (q + 1) * p
    
    for k in range(len(val)):
        if row[k] < t:
            i = row[k] // (q + 1)
        else:
            i = (row[k] - t) // q + p
        if col[k] < t:
            j = col[k] // (q + 1)
        else:
            j = (col[k] - t) // q + p
        
        # Applying the pooling operation (max)
        # V[i, j] += val[k]
        # V[i, j] = opt(V[i, j], val[k])
        C[i, j] += 1
        V[i, j] = val[k] if abs(val[k]) > abs(V[i, j]) else V[i, j]

    # V_avg = np.divide(V, np.maximum(C, 1))
    for i in range(m):  
        for j  in range(m):  
            if (C[i, j] > 0 ):
                B[i,j] = V[i, j] / C[i, j]
        
    V_csr = csr_matrix(V)
    C_csr = csr_matrix(C)
    B_csr = csr_matrix(B)
    
    return V_csr, B_csr

# Define the max function to be used as opt
def max_func(a, b):
    return max(a, b)

# Test routine
def test_compression(coo_data):
    # Create a COO-format sparse matrix for testing
    # values = np.array([1, 2, 3, 4, 5])
    # rows = np.array([0, 1, 2, 3, 4])
    # cols = np.array([0, 1, 2, 3, 4])
    m = 1024  # Assuming a 5x5 matrix for this example
    opt = np.maximum
    # Call the compression function
    V, C = compression(coo_data,m, opt)
    
    # Print the result matrices
    # print("V matrix:\n", V)
    # print("C matrix:\n", C)
    return V,C

# Run the test
