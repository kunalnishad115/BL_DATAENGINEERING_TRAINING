import numpy as np

data=np.array([12,890,23,78,np.nan,765,np.nan,900,0])

mask=np.isnan(data)

print(data[~mask])