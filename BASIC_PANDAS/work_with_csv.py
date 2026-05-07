import pandas as pd
import numpy as np

series_data = pd.read_csv('BASIC_PANDAS/subs.csv')

series_data_virat=pd.read_csv('BASIC_PANDAS/kohli_ipl.csv',index_col='match_no')

print("Virat Data Series: ",series_data_virat.squeeze())


print(series_data.squeeze())
print(series_data_virat.head(2))
print(series_data_virat.tail(2))
print(series_data.sample(3))
print(series_data_virat.value_counts())
print(series_data_virat.sort_values(by='runs',ascending=True))
