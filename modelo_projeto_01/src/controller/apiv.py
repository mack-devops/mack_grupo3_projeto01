import pandas as pd
import json

df = pd.read_csv('dataset.csv')

def post(request):
    response = {
        "data": "VALOR RETORNADO PELA CONTROLLER QUANDO A SOLICITAÇÃO FOR POST"
    }
    return response


def get():
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados

def get1():
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados

def get2():
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados

def get3():
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados

def get4():
    df.to_json('test.json', orient="records")
    with open('test.json', encoding='utf-8') as meu_json:
        dados = json.load(meu_json)
    return dados
