import requests
import re
import json
import main

api_key = 'fa6a271'
url = 'http://www.omdbapi.com/'


def validate_movie_id(movie_id):
    regex = re.compile(r"^[t]{2}\d+$")
    if movie_id != '' and len(movie_id) != 9:
        return False
    else:
        return bool(regex.search(movie_id))


def fetch_movie_details(movie_id):
    if validate_movie_id(movie_id):
        endpoint = f'{url}?i={movie_id}&apiKey={api_key}'
        movie_details = requests.get(endpoint)
        # json converted to python dict below
        return json.loads(movie_details.text)
    else:
        raise Exception('Please enter the valid movie id')


def fetch_all_movie_details(count):
    movie_ids = main.get_imdb_movie_ids(count)
    movie_details_list = []
    for movie_id in movie_ids:
        result = fetch_movie_details(movie_id)
        movie_details_list.append(result)
    return movie_details_list


# print(fetch_all_movie_details(5))


