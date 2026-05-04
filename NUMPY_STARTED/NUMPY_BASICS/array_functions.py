import numpy as np

a1=np.random.random((4,3))
a1=np.round(a1*100)

a2=np.arange(12).reshape(3,4)
print(a2)

print("Max Vals Colum Wise:",np.max(a2,axis=0)) ## col 
print("Max Vals Row Wise:",np.max(a2,axis=1)) ## row

print("Min Vals Colum Wise:",np.min(a2,axis=0))
print("Min Vals Row Wise: ",np.min(a2,axis=0))

print("Sum Row : ",np.sum(a2,axis=1))
print("Sum col : ",np.sum(a2,axis=0))

print("mean of the matrix: ",np.mean(a2))
print("median of the matrix: ",np.median(a2))
print("standard deviation : ",np.std(a2))
print("variance  : ",np.var(a2))


print("dot Product : ",np.dot(a1,a2))
print("log functions:", np.log(a2))
print("exponential fun:" , np.exp(a2))








# print(a1)