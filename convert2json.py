import csv
import io
import json
import requests


CSV_DATA = (
    "https://docs.google.com/spreadsheets/d/1v99oT7y-PV9Sy7myZ2_XFmohiOuvAAtN11Onp7ZhTq0/"
    "export?gid=786249884&format=csv"
)

def get_data(url):
    r = requests.get(url)
    return r.text


def csv_to_data(csv_data):
    csv_file = io.StringIO(csv_data)
    reader = csv.reader(csv_data)
    for row in reader:
        print(row)
        break
        yield row.decode


def data_to_json(data):
    return json.dumps(list(data))


if __name__ == '__main__':
    csv_stream = get_data(CSV_DATA)
    data = csv_to_data(csv_stream)
    json_data = data_to_json(data)
    print(json_data)
