# covid2json

Prende i dati covid da `https://docs.google.com/spreadsheets/d/1v99oT7y-PV9Sy7myZ2_XFmohiOuvAAtN11Onp7ZhTq0/` e li trasforma in JSON.

Per ora prende solo i dati dei decessi su base provinciale.

## Requisiti

Su una distribuzione basata su Debian dovresti poter usare tutti i pacchetti di sistema:

```
sudo apt install python3 python3-requests
```

Altrimenti crea un virtualenv:

```
python3 -m venv venv
./venv/bin/pip install -r requirements.txt
```

e ricorda di attivarlo quando vuoi chiamare lo script

```
. ./venv/bin/activate
```

## Uso

```
$ python3 convert2json.py > mortalita_per_provincia.json
```
