import movie_details_finder
import movie_synposis_dict


def get_updated_dictionary_with_jsonData():
    list_of_selected_keys_from_json = ['Title', 'Genre', 'Actors', 'imdbID'];
    # Get movie synopsis with imdb ID dictionary
    movie_dict = movie_synposis_dict.generate_movie_synopsis_dict()
    count = len(movie_dict)
    # Adding movie genres and movie actors from the JSON response and
    # updating the above dictionary with genres and actors as keys
    filtered_dict_list = []
    movie_details = movie_details_finder.fetch_all_movie_details(count)
    for movie_detail in movie_details:
        filtered_dictionary = {key: value for key, value in movie_detail.items()
                               if key in list_of_selected_keys_from_json}
        filtered_dict_list.append(filtered_dictionary)
    for i, item in enumerate(filtered_dict_list):
        # if i == len(item):
        #     print('entered')
        #     key = 'keywords'
        #     item[key] = movie_dict.get(list(movie_dict)[i])
        # else:
        key = list(movie_dict)[i]
        print('key', key)
        if key in list_of_selected_keys_from_json:
            item[key] = movie_dict.get(list(movie_dict)[i])
        else:
            item['keywords'] = movie_dict.get(list(movie_dict)[i])
    return filtered_dict_list


print(get_updated_dictionary_with_jsonData())
