import pandas as pd

data = {
    'date': [
        '2026-01-01',
        '2026-01-02',
        '2026-01-03',
        '2026-02-01',
        '2026-02-02',
        '2026-02-03',
        '2026-03-01',
        '2026-03-02'
    ],

    'stock_name': [
        'TCS',
        'TCS',
        'TCS',
        'INFY',
        'INFY',
        'INFY',
        'RELIANCE',
        'RELIANCE'
    ],

    'open_price': [
        3500,
        3550,
        3600,
        1500,
        1520,
        1510,
        2500,
        2550
    ],

    'close_price': [
        3550,
        3600,
        3580,
        1525,
        1500,
        1540,
        2580,
        2520
    ]
}

df=pd.DataFrame(data)
print(df)

df['daily_return']=((df['close_price']-df['open_price'])/df['open_price'])*100

# print(df)

top_lose=df['daily_return'].min()
print("LOse--> ",top_lose)

top_gain=df['daily_return'].max()
print('Top Gain --> ',top_gain)

df['rolling_volatility'] = (
    df['daily_return']
    .rolling(3)
    .std()
)
print(df)