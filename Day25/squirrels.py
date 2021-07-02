import pandas as pd

data = pd.read_csv("Day25\dataS.csv")
gray = len(data[data["Primary Fur Color"]=="Gray"])
red = len(data[data["Primary Fur Color"]=="Cinnamon"])
black = len(data[data["Primary Fur Color"]=="Black"])

print(gray)
print(red)
print(black)

data_dict = {
    "Fur Color": ["Gray","Cinnamon","Black"],
    "Count" : [gray,red,black]
}

df = pd.DataFrame(data_dict)
df.to_csv("Day25\Squirrels.csv")

