import pandas as pd

# ○ Null values
# ○ Duplicate values
# Handle missing values.
# ● Remove duplicate rows.
# ● Replace invalid values like:
# ○ inf
# ○ null
# ○ 0 where necessary

## ----------------------------->>>>>>>>>>>>>

# ● Total confirmed cases
# ● Total deaths
# ● Total recovered cases
# ● WHO region wise analysis
# ● Highest active cases
# ● Top 10 affected regions
# Use:
# ● groupby()
# ● sorting
# ● filtering
# ● aggregation functions


class Task:
  def __init__(self,path_csv):
    self.df=pd.read_csv(path_csv)

  def info_about_dataFrame(self):
    print(self.df.info())

  def data_pre_processing(self):
    print("Total Null values", self.df.isnull().sum())
    print("Total Duplicate Values: ",self.df.duplicated().sum())
    
  def data_cleaning(self):
    print("Removed Duplicate Rows",self.df.drop_duplicates())
    print("Replaced The NAN/Null Values: ", self.df.fillna(0))

  def total_confiemed_EDA(self):
    total_cofirmed_case=self.df['Confirmed'].sum()
    print(total_cofirmed_case)
  def total_deaths_EDA(self):
    total_deaths=self.df['Deaths'].sum()
    print("TOTAL Deaths: ",total_deaths)

  def total_recover_EDA(self):
    total_recover_cases=self.df['Recovered'].sum()
    print("Total Recover Cases: ",total_recover_cases)

  def who_region_EDA(self):
    who_region_analysis=self.df.groupby('WHO Region')['Confirmed'].sum()
    print(who_region_analysis)

  def highest_active_EDA(self):
    high_active_case=self.df.sort_values(by='Active',ascending=False).head(1)
    print(high_active_case)

  def top_effected_EDA(self):
    top_affected=self.df.sort_values(by='Confirmed',ascending=False).head(10)
    print(top_affected)
  
  def start_analysis(self):
    self.info_about_dataFrame()
    self.data_pre_processing()
    self.data_cleaning()
    self.total_confiemed_EDA()
    self.total_deaths_EDA()
    self.total_recover_EDA()
    self.who_region_EDA()
    self.highest_active_EDA()
    self.top_effected_EDA()
    
obj=Task("EXERCISE_VIS/country_wise_latest.csv")
obj.start_analysis()
    


