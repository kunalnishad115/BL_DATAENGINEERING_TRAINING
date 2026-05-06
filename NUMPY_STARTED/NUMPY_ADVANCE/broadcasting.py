import numpy as np

array_1=np.arange(3).reshape(1,3)
array_2=np.arange(4).reshape(4,1)

# a = np.array([[1,2,3],
#             [4,5,6]])

# b = np.array([10,20,30])

# print(a + b)


# a = np.ones((3,4))
# b = np.arange(4)

# print(a + b)


# a = np.ones((3,4))
# b = np.arange(3).reshape(3,1)

# print(a + b)

data = np.array([[10,20,30],
                 [40,50,60]])

scale = np.array([1, 0.1, 0.01])

result = data * scale
print(result)


data = np.ones((3,3))
bias = np.array([1,2,3])

result = data + bias
print(result)


a = np.arange(6).reshape(2,3)
b = np.array([[10],[20]])

print(a + b)


a = np.ones((2,3,4))
b = np.ones((4))

print(a + b)