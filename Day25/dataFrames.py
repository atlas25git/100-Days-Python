#entire csv file is termed as a dataframe
#every single column is a series

import pandas as pd

data=pd.read_csv("Day25\weather_data.csv")
print(data)
table = data["temp"].to_list()
print(table)

# thwere are various methods as .max, .min

#retrieveing data in cols

print(data["condition"])
print(data.condition)

print("Getting data in rows")

print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])

#Creating dataFrame from dictionary
data_d = {
    "Students":["A","B","C"],
    "Class":[1,2,3]
}
data = pd.DataFrame(data_d)
print(data)
data.to_csv("Day25\\file.csv")
