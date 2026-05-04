import numpy as np

a1=np.arange(12).reshape(3,4)
# a1=np.arange(10)
a2=np.arange(12,24).reshape(3,4)

print(a1*5) ## scaler operations 
print(a2-20)

print(a1==5) ## relationship operations
print(a1>5)

print(a1+a2) ## Vectorisation operations 
print(a1-a2)


