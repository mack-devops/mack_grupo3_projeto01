import pandas as pd
import json

df = pd.read_csv('./src/controller/dataset.csv')
df1 = df.groupby('car_make').agg({'car_value':'mean'})

def post(request):
    response = {
        "data": "VALOR RETORNADO PELA CONTROLLER QUANDO A SOLICITAÇÃO FOR POST"
    }
    return response


def get():
    df.to_json('./src/controller/test.json', orient="records")
    with open('./src/controller/test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados


def get1():
<<<<<<< HEAD
    df1.to_json('test.json1', orient="records")
    with open('test.json1', encoding='utf-8') as meu_json1:
=======
    df1.to_json('./src/controller/test.json1', orient="records")
    with open('./src/controller/test.json1', encoding='utf-8') as meu_json1:
>>>>>>> 3a7d5f214fa34d4e82867886b7720ca160c25862
        dados = json.load(meu_json1)
    return dados

def get2(request):
<<<<<<< HEAD
    df.to_json('test.json2', orient="records")
    with open('test.json2', encoding='utf-8') as meu_json2:
=======
    filtro = request.json['value']
    df.to_json('./src/controller/test.json2', orient="records")
    with open('./src/controller/test.json2', encoding='utf-8') as meu_json2:
>>>>>>> 3a7d5f214fa34d4e82867886b7720ca160c25862
        dados = json.load(meu_json2)
    return dados

def get3():
    df.to_json('./src/controller/test.json3', orient="records")
    with open('./src/controller/test.json3', encoding='utf-8') as meu_json3:
        dados = json.load(meu_json3)
    return dados

def get4():
    df.to_json('./src/controller/test.json4', orient="records")
    with open('./src/controller/test.json4', encoding='utf-8') as meu_json4:
        dados = json.load(meu_json4)
    return dados
