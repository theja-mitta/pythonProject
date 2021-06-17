import csv
import movie_dict_updater


def convert_dict_to_csv():
    final_dictionary_list = movie_dict_updater.get_updated_dictionary_with_jsonData()
    keys = final_dictionary_list[0].keys()
    print(keys)
    print('&&&&&&&&&&')
    print(final_dictionary_list)
    try:
        with open('movies.csv', 'w', newline='') as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(final_dictionary_list)
    except IOError as err:
        print(err)


convert_dict_to_csv()
