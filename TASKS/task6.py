import pandas as pd
data = {
    'patient_id': [
        101,102,103,101,
        102,103,104,105
    ],

    'timestamp': [
        '2026-05-01 08:00',
        '2026-05-01 08:10',
        '2026-05-01 08:20',
        '2026-05-01 09:00',
        '2026-05-01 09:10',
        '2026-05-01 09:20',
        '2026-05-01 09:30',
        '2026-05-01 09:40'
    ],

    'heart_rate': [
        72,
        80,
        76,
        130,
        82,
        150,
        95,
        170
    ],

    'ward': [
        'ICU',
        'General',
        'ICU',
        'ICU',
        'General',
        'ICU',
        'Emergency',
        'Emergency'
    ]
}

df = pd.DataFrame(data)

print(df)

avg_rate_ward=df.groupby('ward')['heart_rate'].mean()
print(avg_rate_ward)

df['prev_heart_rate']=df.groupby('patient_id')['heart_rate'].shift(1)

# print(df)

df['spikes_heart_rate']=(df['heart_rate']-df['prev_heart_rate'])

print(df)

mask=df['heart_rate']>120

print(df[mask])