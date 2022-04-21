import requests
from bs4 import BeautifulSoup

response = requests.get(url="https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page,'html.parser')
# print(soup.prettify())
movies_list = []
movie_names= soup.find_all(name="h3", class_="title")
for movie in movie_names:
    movies_list.append(movie.get_text())
movies_list.reverse()
print(movies_list)

with open("movies.txt", mode="w") as movies:
    for movie in movies_list:
        movies.write(f"{movie}\n")
