import numpy as np
np.random.seed(1)
data=np.random.randint(20,45,size=(7,24))
print(data)

max_temp=data.max(axis=1)
print(max_temp)

min_temp=data.min(axis=1)
print(min_temp)

var=max_temp-min_temp
print(var)

largest_var=np.argmax(var)
print(largest_var)

mean_data=data.mean()
std_data=data.std()

lower_limit = mean_data - 2 * std_data
upper_limit = mean_data + 2 * std_data


data[(data < lower_limit) | (data > upper_limit)] = mean_data

print(data)