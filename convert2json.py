import csv
import io
import json
import requests


CSV_DATA = (
    "https://docs.google.com/spreadsheets/d/1v99oT7y-PV9Sy7myZ2_XFmohiOuvAAtN11Onp7ZhTq0/"
    "export?gid=1902469983&format=csv"
)


def kind_from_place(place):
    """Sorry not sorry"""
    if place == "fr (fuori_regione)":
        return "fuori"
    elif len(place) == 2:
        return "provincia"
    elif place == "TOT ITALIA":
        return None
    elif place == "crescita":
        return None
    else:
        return "regione"


def get_data(url):
    r = requests.get(url)
    return r.text


def csv_to_data(csv_data):
    csv_file = io.StringIO(csv_data)
    reader = csv.DictReader(csv_file, delimiter=",")
    regioni = {}
    province = {}
    for row in reader:
        # FIXME
        place = row.pop("mortalità per provincia")
        kind = kind_from_place(place)
        if not kind:
            continue
        if kind == "regione":
            regioni[place] = dict(province)
            province = {}
        elif kind == "provincia":
            province[place] = row
    return regioni


def data_to_json(data):
    return json.dumps(list(data))


if __name__ == '__main__':
    csv_stream = get_data(CSV_DATA)
    data = csv_to_data(csv_stream)
    json_data = data_to_json(data)
    print(json_data)
