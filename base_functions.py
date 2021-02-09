import locale
import json

def j_scraper(file_path):
    with open(file_path, "r") as json_file:
        data = json.load(json_file)
    return data


def get_language():
    locale.setlocale(locale.LC_ALL, "")
    language = locale.getlocale(locale.LC_MESSAGES)[0][0:2]
    return language