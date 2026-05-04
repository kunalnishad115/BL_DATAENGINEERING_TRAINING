import numpy as np

## 2D matrix

matrix_2d=np.arange(12).reshape(3,4)
matrix_3d=np.arange(27).reshape(3,3,3)

print(matrix_2d)
print(matrix_3d)

print(matrix_2d[1,2])
print(matrix_3d[1,0,1])

print(matrix_2d[0,:])
print(matrix_2d[:,3])

print(matrix_2d[1,::3])
print(matrix_2d[::2,::3])
print(matrix_2d[1:,1::])

print(matrix_3d[0::2,0,0::2])

for i in matrix_2d:
  print(i)

for i in matrix_3d:
  print(i)

for i in np.nditer(matrix_3d):
  print(i)


print(np.transpose(matrix_2d))
print(np.transpose(matrix_3d))
print(matrix_3d.ravel())