import synopsis_nlp_parser
import synopsis_scraper
import main


def generate_movie_synopsis_dict():
    movie_ids = main.get_imdb_movie_ids(2)
    # print(movie_ids)
    synopsis_list = synopsis_scraper.get_synopsis(movie_ids)
    # print(synopsis_list)
    synopsis_nlp_parsed_list = []
    for synopsis in synopsis_list:
        parsed_synopsis = synopsis_nlp_parser.synopsis_parser(synopsis)
        synopsis_nlp_parsed_list.append(parsed_synopsis)
    # print(synopsis_nlp_parsed_list)
    # using dictionary comprehension
    # to convert lists to dictionary
    movie_synopsis_dict = {movie_ids[i]: synopsis_nlp_parsed_list[i] for i in range(len(movie_ids))}
    # update_dictionary_with_jsonData(len(movie_ids))
    return movie_synopsis_dict
