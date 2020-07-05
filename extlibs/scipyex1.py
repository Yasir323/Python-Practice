# Program to create sparse Matrix using CSR format
import numpy as np
from scipy import sparse
# Create a 2D Numpy array with a diagonal of ones and rest zeros
eye = np.eye(4)
print("Numpy array:\n{}".format(eye))
# Convert the NumPy array to a SciPy sparse matrix in CSR format
# Only the nonzero entries are stored
sparse_matrix = sparse.csr_matrix(eye)
print("\nScipy sparse CSR Matrix:\n{}".format(sparse_matrix))
