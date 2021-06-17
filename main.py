import requests
from bs4 import BeautifulSoup


def get_imdb_movie_ids(count):
    try:
        url = 'http://www.imdb.com/chart/top'
        res = requests.get(url, verify=False)
        movies_chart = BeautifulSoup(res.text, 'html.parser')
        movies_list = movies_chart.body.find("tbody", {"class": "lister-list"})
        movies_list_items = movies_list.find_all('tr')
        movie_ids = []

        for i, chart_row in enumerate(movies_list_items):
            while i < count:
                movie_id = chart_row.find("div", {"class": "seen-widget"})['data-titleid']
                movie_ids.append(movie_id)
                break

        return movie_ids

    except Exception as err:
        print(err)


if __name__ == '__main__':
    print('Main page')
