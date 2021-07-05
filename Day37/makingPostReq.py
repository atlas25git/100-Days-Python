#request.get()
#request.post()

import requests 
import html

url = "https://shielded-mountain-60766.herokuapp.com/posts"
res = requests.get(url)

data = open("Day37/articles.txt","a")

#print(len(res.json()))
for n in range(len(res.json())):
    data.write(html.unescape(res.json()[n]["title"]))
    data.write("\n")
    data.write("______________________")
    data.write("\n")
    data.write(html.unescape(res.json()[n]["content"]))
    data.write("\n")

    

#print(res.json()[0]["title"]

##advanced authentication using http
#using http header
headers = {
    "userApiId": Token
}

res1 = requests.post(url=gc,json=gc,headers=headers)