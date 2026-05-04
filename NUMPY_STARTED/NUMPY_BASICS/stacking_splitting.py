import numpy as np

matrix_2d=np.arange(12).reshape(3,4)
matrix_3d=np.arange(12).reshape(3,4)

print(np.hstack((matrix_2d,matrix_3d)))
print(np.vstack((matrix_2d,matrix_3d)))

# print(np.hsplit(matrix_2d, 4))   
# print(np.vsplit(matrix_3d, 2))
