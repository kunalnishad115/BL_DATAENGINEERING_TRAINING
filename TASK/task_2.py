# | Employee | Q1 | Q2 | Q3 | Q4 |
# | -------- | -- | -- | -- | -- |
# | Emp1     | 4  | 5  | 3  | 4  |
# | Emp2     | 2  | 3  | 4  | 1  |


import numpy as np
np.random.seed(1)

data=np.random.randint(1,6,size=(100,4))
print(data)

min_val=data.min()
max_val=data.max()



normalized_rating=(data-min_val)/(max_val-min_val)

print(normalized_rating)

emp_avg=normalized_rating.mean(axis=1)
print(emp_avg)

cmp_mean=emp_avg.mean()
print(cmp_mean)

high_per=np.where(emp_avg>cmp_mean)

print(high_per)


