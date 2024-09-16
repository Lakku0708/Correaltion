import numpy as np
N = 4
vec1 = np.random.rand(N)
vec2 = np.random.rand(N)
correlation_matrix = np.corrcoef(vec1, vec2)
correlation = correlation_matrix[0, 1]

# Output
print("Vector 1:", vec1)
print("Vector 2:", vec2)
print("Correlation between Vector 1 and Vector 2:", correlation)
