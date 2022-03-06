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

pastaLeitura = '/.files/'

try:
    df = pd.read_csv(pastaLeitura + 'dataset.csv')
except:
    df = pd.read_csv('dataset.csv')

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
