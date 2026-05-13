import pandas as pd
import numpy as np

data_set={
  'id':[1,2,3,4,5,6],
  'names':['kunal','ram','shyam',np.nan,np.nan,'rahul'],
  'marks':[90,97,np.nan,np.nan,np.nan,89]
}

student=pd.DataFrame(data_set)
print(student)


## find the missing values

print(pd.isna(student).sum())

## remove the missing values

print(student.dropna())

## filling missing values
student.loc[student['names'].isnull(), 'names'] = ['ram', 'kirti']

print(student)

