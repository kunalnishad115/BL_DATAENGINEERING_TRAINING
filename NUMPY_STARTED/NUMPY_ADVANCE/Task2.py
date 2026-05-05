import numpy as np
transactions = np.array([500, 2000, 15000, 7000, 25000])
mask = transactions > 10000
ans=transactions[mask]

print("Suspecious Ammount: ",ans)
print(ans.size)