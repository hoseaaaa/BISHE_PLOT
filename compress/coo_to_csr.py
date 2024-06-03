from scipy.sparse import coo_matrix

# Function to convert COO to CSR format
def coo_to_csr(coo_data):
    csr_data = coo_data.tocsr()
    return csr_data

# Test routine to convert COO to CSR
def test_coo_to_csr():
    # Create a COO-format sparse matrix for testing
    coo = coo_matrix(([1, 2, 3, 4], ([0, 1, 2, 3], [0, 1, 2, 3])), shape=(4, 4))
    
    # Convert COO to CSR
    csr = coo_to_csr(coo)
    
    # Return the CSR representation

    return csr.data, csr.indices, csr.indptr

# Run the test and print the results
test_coo_to_csr()
