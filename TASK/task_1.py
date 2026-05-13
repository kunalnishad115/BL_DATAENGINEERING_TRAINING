import numpy as np

np.random.seed(1) ## ye meri random matrix ko fix kr dega 
data=np.random.randint(-100,200 ,size=(30,5))
print(data)

mask=data<0
data[mask]=0
print(data)

# Week1 → day 1–7
# Week2 → day 8–14
# Week3 → day 15–21
# Week4 → day 22–28

avg_sales=data[:28]
tensor=avg_sales.reshape(4,7,5)

avg_sales_pro=tensor.mean(axis=0)
print(avg_sales_pro)

highes_pro_avg=np.argmax(avg_sales_pro)
print(highes_pro_avg)

