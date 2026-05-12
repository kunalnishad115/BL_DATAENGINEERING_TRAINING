import pandas as pd

data={
  'order_id':[1,2,3,4,5,6],
  'customer_id':[123,345,234,565,432,454],
  'order_date':['14-jan-2024','15-jan-2024','4-jan-2024','23-jan-2024','7-jan-2024','31-jan-2024'],
  'order_amount':[1000,2000,2003,4599,100,2319],
}

reatail=pd.DataFrame(data)
print(reatail)
reatail.shape

reatail['order_date']=pd.to_datetime(reatail['order_date'])

reatail['month']=reatail['order_date'].dt.month_name()
print(reatail)

total_revenue=reatail.groupby('month')['order_amount'].sum()
print(total_revenue)

total_unique=reatail.groupby('month')['customer_id'].unique()
print(total_unique)

