# #working with apis in python
# #needs to be installed
# import requests

# response = requests.get(url="someURL")
# response.raise_for_status()#will create exceptions

# data = response.json()["valueAttrName"]

# print(response)



# #response have several properties

# if response.status_code != 200:
#     raise Exception("Not working")

# requests module could be used to raise exceptions

#using split
s = "NeonGraveDontStartACult"
print(s.split("G")[1].split("D"))
