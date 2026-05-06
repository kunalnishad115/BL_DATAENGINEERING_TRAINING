import numpy as np

balances = np.array([500, 2500, 8000, 1500, 6000])


risk = np.where(
    balances < 2000, "High Risk",
    np.where(balances <= 7000, "Medium Risk", "Low Risk")
)

print(risk)