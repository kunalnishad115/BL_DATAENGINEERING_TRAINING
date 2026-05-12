import pandas as pd

data={
  'emp_id':[101,102,103,104,105,106,107,108,
            109,110,111,112],
  'department':[
    'HR','HR','HR','HR',
    'IT','IT','IT','IT',
    'Sales','Sales','Sales','Sales'
  ],
  'quarter':[
    'Q1','Q2','Q3','Q4',
    'Q1','Q2','Q3','Q4',
    'Q1','Q2','Q3','Q4'
  ],
  'performance_score':[
    60,65,70,75,      
    80,78,82,85,      
    50,55,60,68
  ]
}

emp=pd.DataFrame(data)
print(emp)

group_avg=emp.groupby(['department','quarter'])['performance_score'].mean()

print(group_avg)

