import numpy as np

actual_array=np.random.randint(1,100,15)
predicted_array=np.random.randint(1,100,15)

def mse(actual_array,predicted_array):
  return np.mean((actual_array-predicted_array)**2)
  

print(mse(actual_array,predicted_array))

