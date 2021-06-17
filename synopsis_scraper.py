from main import get_imdb_movie_ids
import requests
from bs4 import BeautifulSoup

imdb_movie_page_url = 'https://www.imdb.com/title/'

synopsis_list = []


def get_synopsis(movie_ids_list):
    for movie_id in movie_ids_list:
        url = f'https://www.imdb.com/title/{movie_id}'
        res = requests.get(url, verify=False)
        movie_content = BeautifulSoup(res.text, 'html.parser')
        synopsis = movie_content.find('p', {"data-testid": "plot"}).findChild('span').getText()
        synopsis_list.append(synopsis)
    return synopsis_list