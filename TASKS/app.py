import pandas as pd
import numpy as np

country=pd.read_csv(r'TASKS/Countries.csv')
print(country.shape)
# print(country)

# print(country.info())
# print(country.describe())

# print(country.isna().sum())


need_fill=country[country['title'].isna()==True]
# print(need_fill.fillna(0))

## highest countary pop

print(country[country['population']==country['population'].max()]['country'])

## min countay pop

print(country[country['population']==country['population'].min()]['population'])

## top 5 countary with high democratic rate 

cnt_name=country['democracy_score'].sort_values(ascending=False).head(3)

# country[cnt_name]

## n largest country pop

mask=country['population']==country['population'].nlargest(2).iloc[1]
print(country[mask])





