from bs4 import BeautifulSoup
import requests

file = open("Day45/self/new.txt","a")

res = requests.get("https://bitmesra.ac.in/Visit_Other_Department_9910?cid=1&deptid=183&pid=10");
soup = BeautifulSoup(res.content,"html.parser")
content = soup.select("tr td ul li a")

urlStrt = "https://bitmesra.ac.in/"
listHref = []
for tag in content:
    listHref.append(tag.get("href"))

for n in listHref:
    file.write(urlStrt + n)
    file.write("\n")

print(listHref)
#print(content)