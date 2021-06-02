# importing Numpy package
import numpy as np

# creating a 3X3 Numpy matrix
n_array = np.array([[0, 2, 5],
                    [2, 1, 1],
                    [3, 1, 0]])

# Displaying the Matrix
print("Numpy Matrix is:")
print(n_array)

# calculating the determinant of matrix
det = np.linalg.det(n_array)

print("\nDeterminant of given 3X3 matrix:")
print(float(det))

------------------------------------------------
# Output
# Numpy Matrix is:
# [[0 2 5]
#  [2 1 1]
#  [3 1 0]]

# Determinant of given 3X3 matrix:
# 0.9999999999999991
