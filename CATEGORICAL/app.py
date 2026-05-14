import pandas as pd
import numpy as np
import seaborn as sea
import matplotlib.pyplot as plt

df=sea.load_dataset('tips')
# print(df)

## total_bill   tip     sex smoker   day    time  size

# sea.countplot(x=df['sex'],hue=df['smoker'])

# sea.barplot(data=df,x='sex',y='tip',estimator=np.sum)

# sea.violinplot(data=df,x='sex',y='tip')

sea.violinplot(x='day',y='tip')















plt.show()