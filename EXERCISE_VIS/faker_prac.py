from faker import Faker
import pandas as pd

fake = Faker()
Faker.seed(42)
data = []

for i in range(5):
    data.append({
        "Name": fake.name(),
        "Email": fake.email(),
        "City": fake.city(),
        "Salary": fake.random_int(min=30000, max=120000)
    })

df = pd.DataFrame(data)

print(df)