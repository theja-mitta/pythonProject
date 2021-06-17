import logging

import bucket_reader
import main
import pandas
import io
import movie_details_finder


def validate_movie_ids_with_ids_from_csv(ids_from_csv, movie_ids):
    ids_from_csv.sort()
    movie_ids.sort()
    if ids_from_csv == movie_ids:
        print('Ids are identical, So no new movie found from imdb. Hence no change to csv file on s3')
    else:
        # fetch id not matched
        new_ids_found = movie_ids - ids_from_csv
        logging.warning(new_ids_found)
        for new_id in new_ids_found:
            # to do: With new ID make an api call to OMDB API using movie_details_finder module
            # and get specific movie details then append it to csv & upload to s3
            pass


def fetch_id_from_csv(csv_file):
    ids_list = []
    df = pandas.read_csv(io.BytesIO(csv_file['Body'].read()), encoding='utf8')
    # User list comprehension to create a list of lists from Dataframe rows
    list_of_rows = [list(row) for row in df.values]
    for list_row in list_of_rows:
        for item in list_row:
            if movie_details_finder.validate_movie_id(item):
                ids_list.append(item)
            else:
                continue
    return ids_list


def write_bucket():
    """
    # download csv from bucket
    # read csv and get imdbIds
    # get top 5 movies from imdbID by scraping
    # compare if any id is mismatching
    # if mismatch observed then get movie details of that movie using api
    # then update csv with new row
    # then overwrite the csv file on s3 bucket
    """
    csv_file = bucket_reader.download_file('movies.csv', 'vemitta-datascrape')
    ids_from_csv = fetch_id_from_csv(csv_file)
    # get movie_ids of top 5 movie using web scraping module
    movie_ids = main.get_imdb_movie_ids(2)
    validate_movie_ids_with_ids_from_csv(ids_from_csv, movie_ids)


write_bucket()
