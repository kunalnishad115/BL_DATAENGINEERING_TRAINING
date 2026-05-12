import pandas as pd

data={
  'student_id':[1,2,3,1,4,5,2,6],

    'course_id':['Python','Java','Python',
                'SQL','Java','SQL',
                'Python','ML'],

    'login_date':[
        '2026-05-01',
        '2026-05-02',
        '2026-05-05',
        '2026-05-06',
        '2026-05-07',
        '2026-05-08',
        '2026-05-10',
        '2026-05-11'
    ],

    'minutes_spent':[50,60,45,100,30,80,120,90]
}

df=pd.DataFrame(data)
print(df)

df['login_date']=pd.to_datetime(df['login_date'])

latest_date=df['login_date'].max()
print(latest_date)

mask=(latest_date-df['login_date']).dt.days>7
print(df[mask])

avg_session=df.groupby('course_id')['minutes_spent'].mean()
print(avg_session)

engagment=df.groupby('course_id')['minutes_spent'].sum()
print(engagment)

ans=engagment.sort_values(ascending=False).head(3)
print(ans)