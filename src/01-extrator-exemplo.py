#!/usr/bin/env python3

import os
import unicodecsv as csv

# Variáveis principais
outputDir = '../package/data/'

# Exemplo de curso
curso = {}
curso['bolsa_integral_ampla'] = '1'
curso['bolsa_integral_cotas'] = '1'
curso['bolsa_parcial_ampla'] = ''
curso['bolsa_parcial_cotas'] = ''
curso['campus_external_id'] = '9912'
curso['campus_nome'] = "ACRELANDIA - Centro"
curso['cidade_busca'] = "Acrelandia"
curso['cidade_filtro'] = "MTIwMjAwNDAwMDEz"
curso['curso_busca'] = "Administração"
curso['curso_id'] = "99121003265"
curso['grau'] = "Bacharelado"
curso['id'] = '29118'
curso['mensalidade'] = "289.00"
curso['nome'] = "Administração"
curso['nota_integral_ampla'] = "572.74"
curso['nota_integral_cotas'] = "548.00"
curso['nota_parcial_ampla'] = ''
curso['nota_parcial_cotas'] = ''
curso['turno'] = "Curso a Distância"
curso['uf_busca'] = "AC"
curso['universidade_nome'] = "Universidade Paulista - UNIP"

# Lista de cursos
cursos = [curso] * 4

# Cria diretório de saída, se não existe
if not os.path.exists(outputDir):
    os.makedirs(outputDir)

# Escreve curso no arquivo CSV
with open(outputDir+'cursos-prouni.csv', 'wb') as f:
    w = csv.DictWriter(f, cursos[0].keys())
    w.writeheader()
    for curso in cursos:
        w.writerow(curso)
print("... Arquivos CSV criados.")

# Criar o datapackage.json
import json
with open("metadata.json", "r") as mfd:
    output = json.load(mfd)

    with open("resources.json", "r") as rfd:
        output['resources'] = json.load(rfd)
    
    with open("../package/datapackage.json", "w") as datapackage:
        json.dump(output, datapackage, indent=2)
print("... datapackage.json criado.")