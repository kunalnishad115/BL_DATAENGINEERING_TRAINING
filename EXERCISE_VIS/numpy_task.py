import pandas as pd
import numpy as np



class NumpyPrac:
  def __init__(self):
    pass

  def compute(self,array):
    print("Confirmed array:", array)

    print("Mean of Array:",np.mean(array))

    print("Sum of array:",np.sum(array))

    print("Max of Array:",np.max(array))

    print("Min of Array:",np.min(array))

    print(np.size(array))

    print("Reshape the array:",array.reshape(1,-1))

    print("Slicing the array:",array[0:10])

    print("Broadcasting the array:",array+1000)

obj=NumpyPrac()
df=pd.read_csv('EXERCISE_VIS/country_wise_latest.csv')
array=df['Confirmed'].values
obj.compute(array)

