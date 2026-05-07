import numpy as np

def sigmoid_fun_calci(array):
  return 1/1+np.exp(-(array))

array=np.array([1,2,3,4,5,10,24,89])

print(sigmoid_fun_calci(array))

