from faker import Faker
import pandas as pd
import random

fake = Faker()

data = []

for i in range(1000):
    data.append({
        "emp_id": i + 1,
        "name": fake.name(),
        "email": fake.email(),
        "city": fake.city(),
        "salary": random.randint(30000, 120000)
    })

df = pd.DataFrame(data)

df.to_csv("employees.csv", index=False)

print("CSV Generated Successfully")