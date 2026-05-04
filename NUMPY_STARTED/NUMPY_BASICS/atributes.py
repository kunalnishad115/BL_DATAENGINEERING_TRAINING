import numpy as np

a1=np.arange(10)
a2=np.arange(12).reshape(3,4)
a3=np.arange(8).reshape(2,2,2)

print(a1.ndim)
print(a2.ndim)
print(a3.ndim)

print(a1.shape)
print(a2.shape)
print(a3.shape)


print(a1.size)
print(a2.size)
print(a3.size)

print(a1.itemsize)
print(a2.itemsize)
print(a3.itemsize)

# print(a3.dtype)
a3.astype(np.int32)
print(a3.dtype)