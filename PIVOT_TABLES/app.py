import pandas as pd
import numpy as np

data={
  'name':['kunal','rahul','priya'],
  'dept':['IT','MNG','HR'],
  'salery':['60000','70000','40000'],
  'city':['delhi','delhi','hyderabad']

}

emp=pd.DataFrame(data)
print(emp)

pivot_table=pd.pivot_table(emp,index='dept',values='salery',aggfunc='sum')

print(pivot_table)

cross_tab=pd.crosstab(emp['dept'],emp['city'])
print(cross_tab)

