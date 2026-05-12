import pandas as pd

data = {
    'date': [
        '2025-01-01',
        '2025-01-02',
        '2025-01-03',
        '2025-01-04',
        '2025-01-05',
        '2025-01-06',
        '2025-01-07',
        '2025-01-08'
    ],

    'city': [
        'Delhi',
        'Mumbai',
        'Kolkata',
        'Chennai',
        'Delhi',
        'Mumbai',
        'Kolkata',
        'Chennai'
    ],

    'temperature': [
        18,
        30,
        25,
        33,
        17,
        31,
        26,
        34
    ],

    'humidity': [
        55,
        80,
        72,
        68,
        50,
        82,
        70,
        65
    ]
}

temp=pd.DataFrame(data)
print(temp)

print(temp[temp['city']=='Delhi'])

temp['avg_temp_roll_3days']=temp['temperature'].rolling(3).mean()

print(temp)

temp['prev_humidity'] = temp['humidity'].shift(1)

temp['humidity_increased'] = (
    temp['humidity'] > temp['prev_humidity']
)

mask=temp['humidity_increased']

print(temp[mask])



# ncreased
# 1  2025-01-02  Mumbai  ...           55.0                True
# 5  2025-01-06  Mumbai  ...           50.0                True