import os
os.system('cls' if os.name == 'nt' else 'clear')
import pandas as pd

df = pd.read_csv('../../data/unclean_data.csv')

# Clean Duration column
df.dropna(subset=['Duration'], inplace=True) # drop rows where Duration is NaN
for x in df.index:
  if df.loc[x, 'Duration'] > 100 and df.loc[x, 'Duration'] < 0:
    df.drop(x, inplace=True)
mean_duration = df['Duration'].mean()
df.fillna({"Duration": mean_duration}, inplace=True)

# Clean Date column
df.dropna(subset=['Date'], inplace=True) # drop rows where date is NaN
df['Date'] = pd.to_datetime(df['Date'], format='mixed')
df.dropna(subset=['Date'], inplace=True) # drop rows where date is NaT

# Clean Maxpulse column
df.dropna(subset=['Maxpulse'], inplace=True) # drop rows where Maxpulse is NaN
for x in df.index:
  if df.loc[x, 'Maxpulse'] > 200 and df.loc[x, 'Maxpulse'] < 0:
    df.drop(x, inplace=True)

# Clean Calories column
df.dropna(subset=['Calories'], inplace=True) # drop rows where Calories is NaN
for x in df.index:
  if df.loc[x, 'Calories'] > 1000 and df.loc[x, 'Calories'] < 0:
    df.drop(x, inplace=True)

# Drop duplicates
df.drop_duplicates(inplace=True)

df.to_csv("../../data/cleaned_data.csv", index=False)