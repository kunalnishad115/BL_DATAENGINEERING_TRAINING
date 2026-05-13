import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

df=sea.load_dataset('tips')
# print(df)

sea.histplot(df['total_bill'])
# plt.show()

sea.histplot(df['tip'])
# plt.show()



