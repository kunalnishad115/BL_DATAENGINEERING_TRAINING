import numpy as np
import time

# list_1=[i for i in range(10000000)]
# list_2=[i for i in range(10000000)]
# list_3=[]
# st=time.time()
# for i in list_1:
#   list_3.append(list_1[i]+list_2[2])
# print("Time Taken by Python List: ",time.time()-st)

np_array1=np.arange(10000000)
np_array2=np.arange(10000000)
st=time.time()
np_array3=np_array1+np_array2
print("Time Taken By the npArray: ",time.time()-st)





  