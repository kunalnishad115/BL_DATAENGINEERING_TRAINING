import pandas as pd
import numpy as np

# import pandas as pd

employee = pd.DataFrame({
    'emp_id': [1, 2, 3, 4],
    'emp_name': ['Kunal', 'Ram', 'Shyam', 'Rahul'],
    'department': ['IT', 'HR', 'Finance', 'Marketing']
})

salary = pd.DataFrame({
    'emp_id': [1, 2, 5],
    'salary': [50000, 60000, 70000]
})
print("INNER: ",pd.merge(employee,salary,on='emp_id',how='inner'))
print("OUTER: ",pd.merge(employee,salary,on='emp_id',how='outer'))
print("RIGHT: ",pd.merge(employee,salary,on='emp_id',how='right'))
print("LEFT: ",pd.merge(employee,salary,on='emp_id',how='left'))


# employee.join(salary,on='emp_id',how='left')

print(pd.concat([employee,salary],axis=1))

