import numpy as np
array=np.random.randint(1,100,24).reshape(6,4)
ans=array[(array>50) & (array%2==0)]
print(ans)


