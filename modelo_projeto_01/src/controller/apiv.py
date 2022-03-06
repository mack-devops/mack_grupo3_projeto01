import pandas as pd
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
from flask import request
import json
import os
<<<<<<< HEAD
>>>>>>> 58e7211 (Update apiv.py)
import json
=======
>>>>>>> eb23dbe (Update apiv.py)

pastaLeitura = '/.files/'
=======
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

<<<<<<< HEAD
df1 = df.groupby('car_make').agg({'car_value':'mean'})
>>>>>>> 99ffc0d84052008201ba3c1132bc1f4d874f8274

def post():

    pasta = './files'
    arquivo = request.files.get("filename")
    nomeArquivo = arquivo.filename
    arquivo.save(os.path.join(pasta, nomeArquivo))

    response = {
<<<<<<< HEAD
        "data": "VALOR RETORNADO PELA CONTROLLER QUANDO A SOLICITAÇÃO FOR POST"
=======
from flask import request
import json
import os

pastaLeitura = 'files/'
try:
    df = pd.read_csv(pastaLeitura + 'dataset.csv')
except:
    df = pd.read_csv('dataset.csv')
    

df1 = df.groupby('car_make').agg({'car_value':'mean'})
=======
>>>>>>> ae933868a5b93f81e3d4b2f1af65121865c0d113

def post():
    pasta = './files'
    arquivo = request.files.get("filename")
    nomeArquivo = arquivo.filename
    arquivo.save(os.path.join(pasta, nomeArquivo))

    response = {
        "data": "Arquivo Gerado com sucesso !"
>>>>>>> 407c818 (Theo Branch)
=======
        "data": "Arquivo Gerado com sucesso !"
>>>>>>> 99ffc0d84052008201ba3c1132bc1f4d874f8274
    }
    return response
<<<<<<< HEAD


def get():
<<<<<<< HEAD
    df.to_json('./src/controller/test.json', orient="records")
    with open('./src/controller/test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados


def get1():

    df1.to_json('test.json1', orient="records")
    with open('test.json1', encoding='utf-8') as meu_json1:
        dados = json.load(meu_json1)
    return dados

def get2(request):
<<<<<<< HEAD
<<<<<<< HEAD
    filtro = request.json['value']
    df.to_json('./src/controller/test.json2', orient="records")
    with open('./src/controller/test.json2', encoding='utf-8') as meu_json2:
=======
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
=======
    df.to_json('test.json2', orient="records")
    with open('test.json2', encoding='utf-8') as meu_json2:
        dados = json.load(meu_json2)
>>>>>>> b280a47 (teste)
    return dados

def get1():
    print(df1)
    df1.to_json('test.json1', orient="records")
    with open('test.json1', encoding='utf-8') as meu_json1:
        dados = json.load(meu_json1)
    return dados

def get2():
    df.to_json('test.json2', orient="records")
    with open('test.json2', encoding='utf-8') as meu_json2:
>>>>>>> 407c818 (Theo Branch)
=======
    df.to_json('test.json2', orient="records")
    with open('test.json2', encoding='utf-8') as meu_json2:
>>>>>>> 99ffc0d84052008201ba3c1132bc1f4d874f8274
        dados = json.load(meu_json2)
    return dados


def get3():
<<<<<<< HEAD
    df.to_json('./src/controller/test.json3', orient="records")
    with open('./src/controller/test.json3', encoding='utf-8') as meu_json3:
=======
    df.to_json('test.json3', orient="records")
    with open('test.json3', encoding='utf-8') as meu_json3:
>>>>>>> 407c818 (Theo Branch)
        dados = json.load(meu_json3)
    return dados

def get4():
<<<<<<< HEAD
<<<<<<< HEAD
    df.to_json('./src/controller/test.json4', orient="records")
    with open('./src/controller/test.json4', encoding='utf-8') as meu_json4:
=======
    df.to_json('test.json4', orient="records")
    with open('test.json4', encoding='utf-8') as meu_json4:
>>>>>>> 99ffc0d84052008201ba3c1132bc1f4d874f8274
        dados = json.load(meu_json4)
    return dados
=======
    df.to_json('test.json4', orient="records")
    with open('test.json4', encoding='utf-8') as meu_json4:
        dados = json.load(meu_json4)
    return dados
>>>>>>> 407c818 (Theo Branch)
=======
>>>>>>> ae933868a5b93f81e3d4b2f1af65121865c0d113
