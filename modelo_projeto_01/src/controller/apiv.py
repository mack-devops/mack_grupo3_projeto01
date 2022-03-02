import pandas as pd
<<<<<<< HEAD
import json

df = pd.read_csv('./src/controller/dataset.csv')

def post(request):
    response = {
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

    pasta = 'files'
    arquivo = request.files.get("filename")
    nomeArquivo = arquivo.filename
    arquivo.save(os.path.join(pasta, nomeArquivo))

    response = {
        "data": "Arquivo Gerado com sucesso !"
>>>>>>> 407c818 (Theo Branch)
    }
    return response


def get():
<<<<<<< HEAD
    df.to_json('./src/controller/test.json', orient="records")
    with open('./src/controller/test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados


def get1():
    df1.to_json('./src/controller/test.json1', orient="records")
    with open('./src/controller/test.json1', encoding='utf-8') as meu_json1:
        dados = json.load(meu_json1)
    return dados

def get2(request):
    filtro = request.json['value']
    df.to_json('./src/controller/test.json2', orient="records")
    with open('./src/controller/test.json2', encoding='utf-8') as meu_json2:
=======
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
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
    df.to_json('./src/controller/test.json4', orient="records")
    with open('./src/controller/test.json4', encoding='utf-8') as meu_json4:
        dados = json.load(meu_json4)
    return dados
=======
    df.to_json('test.json4', orient="records")
    with open('test.json4', encoding='utf-8') as meu_json4:
        dados = json.load(meu_json4)
    return dados
>>>>>>> 407c818 (Theo Branch)
