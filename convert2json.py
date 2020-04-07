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
    if place == "fr (fuori regione)":
        return "provincia"
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
    r.encoding = "utf-8"
    return r.text


def to_iso_date(date):
    month_map = {
        "gen": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "mag": "05",
        "giu": "06",
        "lug": "07",
        "ago": "08",
        "set": "09",
        "ott": "10",
        "nov": "11",
        "dic": "12",
    }

    day, month = date.split('-')
    if len(day) == 1:
        day = '0' + day
    return "2020-{}-{}".format(month_map[month], day)


def csv_to_data(csv_data):
    csv_file = io.StringIO(csv_data)
    reader = csv.DictReader(csv_file, delimiter=",")
    regioni = {}
    province = {}
    for row in reader:
        place = row.pop("mortalità per provincia")
        row.pop("note")
        kind = kind_from_place(place)
        if not kind:
            continue
        if kind == "regione":
            regioni[place] = dict(province)
            province = {}
        elif kind == "provincia":
            province[place] = {to_iso_date(k): v for k,v in row.items()}
    return regioni


def data_to_json(data):
    return json.dumps(data)


if __name__ == '__main__':
    csv_stream = get_data(CSV_DATA)
    data = csv_to_data(csv_stream)
    json_data = data_to_json(data)
    print(json_data)
