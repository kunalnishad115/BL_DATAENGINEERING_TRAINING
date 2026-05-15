import numpy as np
import pandas as pd

# ● Perform:
# ○ Mean
# ○ Sum
# ○ Max
# ○ Min
# ○ Reshaping
# ○ Slicing
# ○ Broadcasting

class Task:
  '''
  constructor load the csv file and provide the np array for mathmatical operations ...
  
  '''
  def __init__(self,file_path):
    self.df=pd.read_csv(file_path)
    self.array=self.df['Confirmed'].values

  def show_array(self):
    print(self.array)

  def stastical_operation(self):
    print("Mean: ", np.mean(self.array))
    print("Max Value: ",np.max(self.array))
    print("Min Value: ",np.min(self.array))
    print("Sum of Values",np.sum(self.array))

  def reshape_array(self):
    print("Resahaped Array:", self.array.reshape(1,-1))

  def slice_array(self):
    print("Sliced Array: ",self.array[0:10])

  def broadcasting(self):
    print("BroasCasting: ",self.array+5)


  def start_analysis(self):
    self.show_array()
    self.stastical_operation()
    self.reshape_array()
    self.broadcasting()

obj=Task("EXERCISE_VIS/country_wise_latest.csv")
obj.start_analysis()





  