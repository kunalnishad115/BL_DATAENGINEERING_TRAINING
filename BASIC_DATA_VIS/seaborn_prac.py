import pandas as pd
import seaborn as sea
import matplotlib.pyplot as plt

df=sea.load_dataset('tips')
print(df)

sea.histplot(df['total_bill'])
plt.show()

plt.subplot(1,2,1)
sea.histplot(df['tip'],kde=True,bins=20)
plt.subplot(1,2,2)
sea.histplot(df['total_bill'],kde=True)

# ## joint Plots....

sea.jointplot(data=df,x='tip',y='total_bill',kind='kde')

# pair Plots....

sea.pairplot(df,kind='kde',hue='sex')

plt.show()





