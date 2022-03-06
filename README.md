# MACKENZIE: GIT - GROUP 3 #
[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)


## Abstract ##
>Criação de API para análise diária de aluguel de carros.
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
---

## Methods
#### [VERBO] - /NomeMetodo 

###  [POST] - **/importData** 
> I.	1 rota deve ser fornecida para importar o arquivo utilizando form-data;

### [GET] - **/**
> Metodo padrão - API online

### [GET] - **/getAll**
> Retorna todos os dados da base

### [GET] - **/getByIdAndName**
> II.	1 rota que retornará o ID e o nome de todos os arquivos importados;

### [GET] - **/getAverageValuebyManufacturer**
> III.	1 rota que retornará o valor médio de todos os carros baseados no fabricante (coluna car_make agrupada pela média dos valores da coluna car_value);

### [POST] - **/getAverageValuebyManufacturerFiltredByValue**
> IV.	1 rota que retornará o valor médio de um fabricante de carro passado como parâmetro no corpo do request (Após o cálculo de I, pode-se filtrar apenas o valor requerido);

### [GET] - **/getAverageValueByCity**
> V.	1 rota que retornará o valor médio de todos os carros baseados nas cidades correspondentes (coluna city agrupada pela média dos valores da coluna car_value);

### [POST] - **/getAverageValueByCityFiltredByValue**
> VI.	1 rota que retornará o valor médio dos carros de uma cidade passada como parâmetro no corpo do request (Após o cálculo de III, pode-se filtrar apenas o valor requerido).
---