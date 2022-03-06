import pandas as pd
from flask import request
import json
import os

df = pd.read_csv('./files/dataset.csv')
df1 = df.groupby('car_make').agg({'car_value': 'mean'})


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
    dfIdName = pd.DataFrame.from_dict(data, orient='columns')
    dfIdName = pd.DataFrame(dfIdName, columns=['id','first_name'])
    data = dfIdName.to_json(orient='records')
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
