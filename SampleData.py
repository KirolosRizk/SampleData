# importing the pandas module 
import pandas as pd

   
# reading csv file from url
# reading the whole file
col = pd.read_csv("https://raw.githubusercontent.com/KirolosRizk/SampleData/main/nba.csv", header = 0)

# reading column by column
name = pd.read_csv("https://raw.githubusercontent.com/KirolosRizk/SampleData/main/nba.csv", header = 0, usecols = ["Name"])
age = pd.read_csv("https://raw.githubusercontent.com/KirolosRizk/SampleData/main/nba.csv", header = 0, usecols = ["Age"])
salary = pd.read_csv("https://raw.githubusercontent.com/KirolosRizk/SampleData/main/nba.csv", header = 0, usecols = ["Salary"])
weight = pd.read_csv("https://raw.githubusercontent.com/KirolosRizk/SampleData/main/nba.csv", header = 0, usecols = ["Weight (kg)"])

# Brief data about the file
print("Info:\n", col.info(), "\n\n")

# Statistical Analysis
print("Statistical Analysis: \n", col.describe(), "\n\n")

# Sorting by salary
print(col.sort_values(by="Salary", ascending=False))

# finding frequency of names (these names are duplicates)
print("Name Frequencies: \n", name.value_counts())

