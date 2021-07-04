#to write on json files
import json
file = open("data.json","r")
wb="wb"
a = "ass"
b= "bass"
nd = {
    wb : {
        "q": a,
        "ps": b,
    }

}

#json.dump(nd,file,indent=4);

#Reading from json

data = json.load(file)
print(type(data))
#Data in json is loaded as a dictionary in python therefore a great help in accessing the stuff

#To append data in json file we use
data.update(nd);
json.dump(data)

#here we read data alter it and then re dump it in the file