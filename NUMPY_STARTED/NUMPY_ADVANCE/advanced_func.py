import numpy as np
array_1d=np.random.randint(0,100,25)
array_2d=np.random.randint(0,100,25).reshape(5,5)
matrix=np.arange(25).reshape(5,5)

print(matrix)

print(np.sort(array_1d,kind='heapsort')[::-1])
print(np.sort(array_1d,kind='heapsort'))

print(np.sort(array_2d,axis=0,kind='mergesort'))
print(np.sort(array_2d,axis=0,kind='mergesort')[::-1])

print("concated matrix:  ",np.concat((array_2d,matrix),axis=0))

# import numpy as np

duplicate_matrix = np.array([
    [1, 2, 2, 2, 1, 1],
    [9, 0, 9, 0, 2, 5]
])

uniq_vals=np.unique(duplicate_matrix)

print(uniq_vals.size)


ans=np.where(array_2d%2==0,'evenNum',array_2d)
print(ans)

print(np.argmax(array_2d))
print(np.argmin(array_2d))

print(np.cumsum(array_2d,axis=1))
print(np.cumprod(array_2d,axis=0))


print(np.histogram(array_1d,bins=[1,5,10,15,20,25,30]))

items_for_search=[10,0,20,23]
print(array_1d[np.isin(array_1d,items_for_search)])
