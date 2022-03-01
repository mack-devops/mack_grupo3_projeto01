# MACKENZIE: GIT - GROUP 3 #
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Abstract ##
Criação de API para análise diária de aluguel de carros.
Rotas da API:
1 - Importação de arquivo utilizando form-data
2 - Retornará o ID e o nome de todos os arquivos importados
3 - Retornará o valor médio de todos os carros baseados no fabricante
4 - Retornará o valor médio de todos os carros baseados nas cidades correspondentes
5 - Retornará o valor médio dos carros de uma cidade passada como parâmetro no Request


## I. Development Requirements ##

### A. Versions ###
Python 3.8

### B. Running Server ###
```bash
$ pip install -r requirements.txt
$ python .
```

### C. Running Tests ###
```bash
$ pip install -r requirements.txt
$ pytest
```

### D. Command to build project in docker ###
```bash
sudo docker build -t mackenzie-group-x .
sudo docker run -p 5001:5001 -d mackenzie-group-x
```
_______________________________________________________
