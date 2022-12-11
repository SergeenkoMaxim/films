from bs4 import BeautifulSoup
import requests
from dictionaries import urls

headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.9; rv:45.0) Gecko/20100101 Firefox/45.0'
      }

list_of_films = []
list_of_links = []

print(*urls, sep='\n')
user_genre = input("Введите жанр: ")

films_file = open(f"{user_genre}.txt", 'w+')
films_file = open(f"{user_genre}.txt", 'a+')

url = urls.get(user_genre)
page = requests.get(url, headers=headers)
soup = BeautifulSoup(page.text, 'lxml')
link = soup.find_all('li', class_='gallery__item gallery__item_virtual')
film = soup.find_all('span', class_='nbl-slimPosterBlock__titleText')


for url in link:
    film_url = f"https://www.ivi.ru/{url.find('a').get('href')}"
    list_of_links.append(film_url)

for f in film:
    list_of_films.append(f.text)

comedy = dict(zip(list_of_films, list_of_links))

for key, value in comedy.items():
    page = requests.get(value, headers=headers)
    soup = BeautifulSoup(page.text, 'lxml')
    discription = soup.find('div', class_='clause__text-inner hidden-children')
    rating = soup.find('div', class_='nbl-ratingPlate__value')
    duration = soup.find('div', class_='watchParams__item')

    films_file.write(f"{key} - {duration.string}г - {rating.string}★\n"
                     f"{discription.next_element.text}"
                     f"\n")

films_file.close()
