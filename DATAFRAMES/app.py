import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

## dict 

dict_data={
  'name':['kunal','aman','shivam','rahul'],
  'marks':['90','87','100','47'],
  'status':['p','p','p','f']
}

students=pd.DataFrame(dict_data)

movies=pd.read_csv('DATAFRAMES/movies.csv').head(5)
print(movies)
ipl=pd.read_csv('DATAFRAMES/ipl-matches.csv').head(5)
print(ipl)

print(movies.shape)
print(movies.index)
print(movies.columns)
print(movies.values)

## functions

print(movies.sample())
print(movies.info())
print(movies.describe())
print(movies.isnull().sum()) ## usefull 
print("duplicate data -------> ",movies.duplicated().sum())


## selecting Colums 

print(movies['actors'])
print(movies[['actors','year_of_release','imdb_rating']])
print(ipl[['Team1','Team2','WinningTeam']])

## selecting Rows

students.set_index('name',inplace=True)


print(ipl.iloc[[0,2]])
print(students)
print("DATA------------->",students.loc[['kunal','aman','rahul']])


## Selecting Both

print(ipl.iloc[0:5,0:3])
print(ipl.loc[0:5,'ID':'Date'])





