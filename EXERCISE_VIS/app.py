import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df=pd.read_csv('EXERCISE_VIS/IPL.csv')
print(df)

# print(df.info())

## Data Processing ----------------->>>>>-----
print(df.isnull().sum())


match_wins=df['match_winner'].value_counts()
print(match_wins)

# sns.barplot(x=match_wins.index, y=match_wins.values,palette='rainbow')
# plt.show()

# sns.countplot(x=df['toss_decision'])
# plt.show()

mask=df['toss_winner']==df['match_winner']
total_toss_match_win=df[mask]['match_id'].count()

percent=(total_toss_match_win*100)/df.shape[0]
print(percent)

won_by_wicket=df['won_by']=='Wickets'
print(df[won_by_wicket]['match_id'].count())

won_by_runs=df['won_by']=='Runs'
print(df[won_by_runs]['match_id'].count())

sns.countplot(x=df['won_by'])
plt.show()

cnt_mvp=df['player_of_the_match'].value_counts().head(5)
print(cnt_mvp)

# # sns.barplot(x=cnt_mvp.index,y=cnt_mvp.values)
# # plt.show()

high_run=df.groupby('top_scorer')['highscore'].sum().sort_values(ascending=False).head(5)
print(high_run)

# # high_run.plot(kind='barh')
# # plt.show()

df['highest_wicket']=df['best_bowling_figure'].apply(lambda x: x.split('--')[0])
# print(df.columns)
df['highest_wicket']=df['highest_wicket'].astype(int)


high_wicket=df.groupby('best_bowling')['highest_wicket'].sum().sort_values(ascending=False).head(5)
print(high_wicket)

# # high_wicket.plot(kind='bar')
# # plt.show()

won_by_high_runs=df[df['won_by']=='Runs'].sort_values(by='margin',ascending=False).head(1)
print(won_by_high_runs[['match_winner','margin']])
print(won_by_high_runs)






