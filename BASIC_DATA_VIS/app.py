import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x=np.linspace(0,10,5)
print(x)
y=x**2


# plt.title("Hello Graph")
# plt.xlabel("X_AXIS")
# plt.ylabel("Y_AXIS")
# plt.plot(x,y)
# plt.show()
# print('hello')
# print('hello world')

plt.subplot(2,2,1)
plt.plot(x,y)
plt.subplot(2,2,2)
plt.plot(y,x)
plt.subplot(2,2,3)
plt.plot(x**0,y)
plt.subplot(2,2,4)
plt.plot(x**2,y**2)
plt.show()





