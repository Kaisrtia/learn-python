import os
os.system('cls' if os.name == 'nt' else 'clear')
import pandas as pd

a = [1, 7, 2]
m = pd.Series(a)
mm = pd.Series(a, index = ["x", "y", "z"])
k = pd.Series({"day1": 420, "day2": 380, "day3": 390})
# print(m[0])
# print(mm['y'])
# print(k['day2'])

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'price': [10000, 7000, 2000]
}
df = pd.DataFrame(mydataset, index = ["car1", "car2", "car3"])
# print(df.loc["car2"])
# print(df.loc[["car1", "car3"]])
# print(df.head(2))

df = pd.read_csv('../../data/data.csv')
print(df.head(10))