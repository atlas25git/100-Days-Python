# with open("Day25\weather_data.csv") as f:
#     data = f.readlines()
#     print(data)

# #Using inbuilt lib

# import csv

# temperatures  = []
# with open("Day25\weather_data.csv") as f:
#     data = csv.reader(f)
#     for row in data:
#         if(row[1]!="temp"):
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas as pd

data=pd.read_csv("Day25\weather_data.csv")
print(data)
print(data["temp"])