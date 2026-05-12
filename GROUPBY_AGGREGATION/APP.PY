import pandas as pd
import numpy as np


employee_data = {
    'emp_id': [101,102,103,104,105,106,107,108,109,110],
    
    'emp_name': [
        'Kunal','Ram','Shyam','Rahul','Aman',
        'Neha','Priya','Simran','Arjun','Rohit'
    ],
    
    'department': [
        'IT','HR','IT','Finance','HR',
        'Finance','IT','Marketing','Marketing','HR'
    ],
    
    'salary': [
        50000,40000,65000,70000,45000,
        75000,62000,55000,58000,47000
    ],
    
    'experience': [
        2,1,4,5,2,
        6,3,2,4,1
    ],
    
    'city': [
        'Delhi','Mumbai','Delhi','Pune','Mumbai',
        'Pune','Delhi','Bangalore','Bangalore','Mumbai'
    ]
}

employees = pd.DataFrame(employee_data)

print(employees)


ans=employees.groupby('department')['salary'].sum()
print(ans)


ans=employees.groupby('experience')['salary'].sum()
print(ans)

print(employees['salary'].agg(['mean','max','min','count','sum']))
