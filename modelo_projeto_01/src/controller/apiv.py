import pandas as pd
from flask import request
import json
import os

pastaLeitura = '/.files/'
import json

df = pd.read_csv('./src/controller/dataset.csv')

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
    }
    return response


def get():
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
        dados = json.load(meu_json)
    return dados


def get3():
    df.to_json('./src/controller/test.json3', orient="records")
    with open('./src/controller/test.json3', encoding='utf-8') as meu_json3:
        dados = json.load(meu_json3)
    return dados

def get4():
    df.to_json('test.json4', orient="records")
    with open('test.json4', encoding='utf-8') as meu_json4:
        dados = json.load(meu_json4)
    return dados
