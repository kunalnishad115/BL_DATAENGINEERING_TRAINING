from faker import Faker
import pandas as pd
import random
import numpy as np

# Initialize Faker
fake = Faker()
Faker.seed(42)
random.seed(42)
np.random.seed(42)

# Categories
warehouses = ["WH-A", "WH-B", "WH-C", "WH-D", "WH-E"]

products = [
    "Laptop",
    "Mobile",
    "Tablet",
    "Monitor",
    "Keyboard",
    "Mouse",
    "Printer",
    "Camera"
]

suppliers = [
    "Supplier-X",
    "Supplier-Y",
    "Supplier-Z",
    "Supplier-A",
    "Supplier-B"
]

rows = []

for _ in range(200):

    warehouse = random.choice(warehouses)
    product = random.choice(products)
    supplier = random.choice(suppliers)

    stock_level = random.randint(20, 500)

    # Introduce missing values (~10%)
    if random.random() < 0.10:
        stock_level = np.nan

    reorder_level = random.randint(50, 250)

    last_updated = fake.date_between(
        start_date="-2y",
        end_date="today"
    )

    # Transport cost generation
    warehouse_cost = {
        "WH-A": 200,
        "WH-B": 400,
        "WH-C": 600,
        "WH-D": 800,
        "WH-E": 1000
    }

    product_cost = {
        "Laptop": 1200,
        "Mobile": 800,
        "Tablet": 900,
        "Monitor": 700,
        "Keyboard": 250,
        "Mouse": 150,
        "Printer": 1100,
        "Camera": 1300
    }

    supplier_cost = {
        "Supplier-X": 150,
        "Supplier-Y": 250,
        "Supplier-Z": 350,
        "Supplier-A": 450,
        "Supplier-B": 550
    }

    base_cost = (
        warehouse_cost[warehouse]
        + product_cost[product]
        + supplier_cost[supplier]
    )

    stock_component = 0 if pd.isna(stock_level) else stock_level * 3

    noise = random.randint(-200, 250)

    transport_cost = (
        base_cost
        + stock_component
        + noise
    )

    rows.append({
        "Warehouse": warehouse,
        "Product": product,
        "Stock Level": stock_level,
        "Reorder Level": reorder_level,
        "Supplier": supplier,
        "Last Updated": last_updated,
        "Transport Cost": round(transport_cost, 2)
    })

# Create DataFrame
df = pd.DataFrame(rows)

# Save CSV
df.to_csv("inventory_logistics_dataset.csv", index=False)

print(df.head())
print("\nDataset Shape:", df.shape)
print("\nCSV saved as inventory_logistics_dataset.csv")