import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

movies=pd.read_csv('DATAFRAMES/movies.csv')
# print(movies)
ipl=pd.read_csv('DATAFRAMES/ipl-matches.csv')
# print(ipl)


## Task 1 -- find the all sesons final winning team name

mask=ipl['MatchNumber']=='Final'
print(mask)

final_clean_data=ipl[mask]
print(final_clean_data[['Season','WinningTeam']])

## Task 2 -- how many superovers have occured

mask_1=ipl['SuperOver']=='Y'
print("Total Super Overs: ",ipl[mask_1].shape[0])

## Task 3 -- how many mathes won csk in kolkata 

mask_2=(ipl['City']=='kolkata')&(ipl['WinningTeam']=='Chennai Super Kings')

print(ipl[mask_2].shape)

## Task 4 -- Toss Winner is Match Winner 

mask_3=ipl['TossWinner']==ipl['WinningTeam']
print(mask_3)

print(ipl[mask_3].shape[0])

percentage=mask_3.mean()*100
print(percentage)