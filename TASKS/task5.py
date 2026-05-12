import pandas as pd

data = {
    'account_id': [
        1001, 1002, 1003, 1001,
        1002, 1004, 1003, 1005
    ],

    'transaction_date': [
        '2026-05-01',
        '2026-05-02',
        '2026-05-03',
        '2026-05-04',
        '2026-05-05',
        '2026-05-06',
        '2026-05-07',
        '2026-05-08'
    ],

    'amount': [
        5000,
        2500,
        7000,
        1500,
        3200,
        4500,
        20000000,
        8000000
    ],

    'transaction_type': [
        'Credit',
        'Debit',
        'Credit',
        'Debit',
        'Credit',
        'Debit',
        'Debit',
        'Credit'
    ]
}

df=pd.DataFrame(data)
print(df)

daily_trans=df.groupby('account_id')['amount'].sum()
print(daily_trans)

account_high_money=daily_trans.max()
account_high_id=daily_trans.idxmax()
print("High Transaction Account",account_high_money,"with account id :",account_high_id)

# threshold = mean_amount + (2 * std_amount)

mean_ammount=df['amount'].mean()

std_amount=df['amount'].std()

threshold_val=mean_ammount+(2*std_amount)

mask=df['amount']>threshold_val

print(df[mask])

