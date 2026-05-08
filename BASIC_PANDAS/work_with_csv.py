import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

series_data = pd.read_csv('BASIC_PANDAS/subs.csv')

series_data_virat=pd.read_csv('BASIC_PANDAS/kohli_ipl.csv',index_col='match_no')

movies_data=pd.read_csv('BASIC_PANDAS/bollywood.csv',index_col='movie').squeeze()
print(movies_data)

print("Virat Data Series: ",series_data_virat.squeeze())


print(series_data.squeeze())
print(series_data_virat.head(2))
print(series_data_virat.tail(2))
print(series_data.sample(3))
print(series_data_virat.value_counts())
print(series_data_virat.sort_values(by='runs',ascending=True))
print("cnt: ",series_data.count())
print(series_data_virat.count())

print(series_data.mean())
print(series_data.mode())
print(series_data.var())
print(series_data.std())
print(series_data.median())
print(series_data.min())
print(series_data.max())
print(series_data_virat.max())
print(series_data.describe())
print(series_data_virat.describe())


# for movie in movies_data.index:
#   print("movie name:",movie)

# for movie in movies_data:
#   print('actor name:' ,movie)

mask=series_data >=200
print(series_data[mask].count())

print(series_data_virat[series_data_virat>100].count())

# series_data.plot()
# plt.show()

# series_data_virat.plot()
# plt.show()

ans=movies_data.value_counts().head(20)
ans.plot(kind='pie')
plt.show()



# print(series_data[mask])
# print(series_data[mask].size)