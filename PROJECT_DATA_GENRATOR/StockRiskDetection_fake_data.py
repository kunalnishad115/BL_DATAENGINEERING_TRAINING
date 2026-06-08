from faker import Faker
import pandas as pd
import random

fake = Faker()

products = [
    "Laptop", "Mouse", "Keyboard", "Monitor", "Printer",
    "Scanner", "Tablet", "Speaker", "Webcam", "Headphones",
    "Router", "SSD", "Hard Disk", "RAM", "Graphics Card"
]

data = []

for i in range(101, 151):  
    data.append({
        "product_id": f"P{i}",
        "product_name": random.choice(products),
        "stock": random.randint(1, 100)
    })

df = pd.DataFrame(data)
df.to_csv("products.csv", index=False)

# print(df.head())