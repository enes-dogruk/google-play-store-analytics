import numpy as np
import pandas as pd
# weather_df = pd.read_excel('6-weather.xlsx')
# print(weather_df.head())
# print(weather_df.tail())
# print(weather_df.describe())

# Working with missing data

# weather_na_df = pd.read_excel('6-weatherna.xlsx')
# print(weather_na_df.head)

# print(weather_na_df.isna())
# print(weather_na_df.describe())
# print(weather_na_df['Paris'].count())
# print(weather_na_df['Paris'].isna())

# group by

df = pd.read_csv('6-employee.csv')
print(df)
print(df.describe())
print(df['Salary'].mean())
print(df.head())
print(df.groupby('Department'))