import pandas as pd
from flask import request
import json
import os

df = pd.read_csv('./files/dataset.csv')

def loadJsonTest():
    df.to_json('./src/controller/test.json', orient="records")
    with open('./src/controller/test.json', encoding='utf-8') as jason_data:
        dados = json.load(jason_data)
    return dados


def getAll():
    data = loadJsonTest()
    return data


def getByIdAndName():
    data = loadJsonTest()
    dfx = pd.DataFrame.from_dict(data, orient='columns')
    dfx = pd.DataFrame(dfx, columns=['id', 'first_name'])
    data = dfx.to_json(orient='records')
    return data


def getAverageValuebyManufacturer():
    data = loadJsonTest()
    dfx = pd.DataFrame.from_dict(data, orient='columns')
    dfx = pd.DataFrame(dfx, columns=['car_make', 'car_value'])
    dfx = dfx.groupby('car_make').agg({'car_value': 'mean'})
    data = dfx.to_json(orient='records')
    return data


def getAverageValuebyManufacturerFiltredByValue(p_car_make):
    data = loadJsonTest()
    dfx = pd.DataFrame.from_dict(data, orient='columns')
    dfx = pd.DataFrame(dfx, columns=['car_make', 'car_value'])
    #filtrando por fabricante
    dfx = dfx.loc[dfx['car_make']== p_car_make]
    dfx = dfx.groupby('car_make').agg({'car_value': 'mean'})
    data = dfx.to_json(orient='records')
    return data


def getAverageValueByCity():
    data = loadJsonTest()
    dfx = pd.DataFrame.from_dict(data, orient='columns')
    dfx = pd.DataFrame(dfx, columns=['city', 'car_value'])
    dfx = dfx.groupby('city').agg({'car_value': 'mean'})
    data = dfx.to_json(orient='records')
    return data

def getAverageValueByCityFiltredByValue(p_city):
    data = loadJsonTest()
    dfx = pd.DataFrame.from_dict(data, orient='columns')
    dfx = pd.DataFrame(dfx, columns=['city', 'car_value'])
    #filtrando por fabricante
    dfx = dfx.loc[dfx['city']== p_city]
    dfx = dfx.groupby('city').agg({'car_value': 'mean'})
    data = dfx.to_json(orient='records')
    return data


def post():
    pasta = './files'
    arquivo = request.files.get("filename")
    nomeArquivo = arquivo.filename
    arquivo.save(os.path.join(pasta, nomeArquivo))

    response = {
        "data": "Arquivo Gerado com sucesso !"
    }
    return response
