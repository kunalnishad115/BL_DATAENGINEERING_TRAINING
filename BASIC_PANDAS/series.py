import numpy as np
import pandas as pd

my_list=['India','USA','Russia','China']

series=pd.Series(my_list)

print(series)
print(series[2])

marks_val=[99,89,100]
subject_keys=['DSA','DBMS','CN']

custom_idx=pd.Series(marks_val,index=subject_keys,name='hello')
## Atributes in Series Object
print(custom_idx)
print(custom_idx.size)
print(custom_idx.name)
print(custom_idx.is_unique)


dict={
  'Noob':62,
  'pro':75,
  'ultra pro':80
}

print(pd.Series(dict))

