import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
all_movies1 = soup.select("div h3")
print(all_movies1)

# movie_titles = [movie.getText() for movie in all_movies]
# movies = movie_titles[::-1]

# with open("Day45/movies1.txt", mode="w") as file:
#     for movie in movies:
#         file.write(f"{movie}\n")