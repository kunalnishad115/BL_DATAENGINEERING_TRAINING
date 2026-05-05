import numpy as np
array=np.arange(36).reshape(6,6)
print(array[[1,3,4]]) ## row retrieve

print(array[:,[1,3,4]]) ## col retrieve
# print(array)