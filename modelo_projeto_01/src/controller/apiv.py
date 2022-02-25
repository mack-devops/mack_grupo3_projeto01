import pandas as pd
import json

df = pd.read_csv('dataset.csv')
df.to_json('test.json', orient = "records")
with open('test.json', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)

# TODO: ESTE É UM EXEMPLO DE IMPLEMENTAÇÃO DA CONTROLLER

def get():
    # TODO: IMPLEMENTE AQUI
    
   # response = {
   #     "data: print(test.json)"
   # }

    return dados

def post(request):
    # TODO: IMPLEMENTE AQUI

    response = {
        "data": "VALOR RETORNADO PELA CONTROLLER QUANDO A SOLICITAÇÃO FOR POST"
    }

    return response
