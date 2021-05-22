import csv
import pandas as pd


data = pd.read_csv('nameList.csv',index_col='student id')
print(data)