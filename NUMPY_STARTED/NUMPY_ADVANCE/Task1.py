import numpy as np ## Data Cleaning in DE
ages = np.array([22, -5, 35, 120, 45, 0])
mask=ages>0

print(ages[mask])
