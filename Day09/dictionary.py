#syntax
dict_name = {
    "Quotes":"Are necessary",
}
print(dict_name["Quotes"])

dict_name["New"] = "entry"
print(dict_name["New"])

for key in dict_name:
    print(key)
    print(dict_name[key])