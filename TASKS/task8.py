import pandas as pd

data = {
    'timestamp': [
        '2026-05-01 10:00',
        '2026-05-01 10:05',
        '2026-05-01 10:10',
        '2026-05-01 10:15',
        '2026-05-01 10:20',
        '2026-05-01 10:25',
        '2026-05-01 10:30',
        '2026-05-01 10:35'
    ],

    'endpoint': [
        '/login',
        '/login',
        '/payment',
        '/payment',
        '/search',
        '/search',
        '/login',
        '/payment'
    ],

    'response_time': [
        120,
        150,
        400,
        450,
        100,
        110,
        300,
        600
    ]
}

df = pd.DataFrame(data)

print(df)


df['timestamp'] = pd.to_datetime(df['timestamp'])


avg_endpoint=df.groupby('endpoint')['response_time'].mean()
print(avg_endpoint)

# SLA threshold=300

mask=avg_endpoint>300
print("SLA : ",avg_endpoint[mask])

df['rolling_avg']=(
  df['response_time'].rolling(3).mean()
)
# print(df)

mask_1=df['rolling_avg']>300


print('degradation: ',df[mask_1])

