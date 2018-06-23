#!/usr/bin/env python3
import requests
import tools
import os

def me_liberte(url, filename , verbose=False):

    if verbose:
        print('Downloading')
        print(url)

    res = requests.get(url)

    with open(os.path.join(tools.output_path, filename), 'w+') as f:
        f.write(res.text)

    tools.generate_resources(filename, verbose=verbose)

    return res


if __name__ == '__main__':    
    
    # Ajuda Gilmar Mendes a libertar esses dados!
    prisioneiros = [
                {'cela':'http://www.ispdados.rj.gov.br/Arquivos/UppEvolucaoMensalDeTitulos.csv',
                'nome': 'evolucao-seguranca-upp-rj.csv',
                'type':'csv'},
                {'cela':'http://www.ispdados.rj.gov.br/Arquivos/ArmasDP2003_2006.csv',
                'nome': 'apreensao-armas-por-dp-rj.csv',
                'type':'csv'},
                ]

    verbose=True
    with tools.Brasilio(verbose=verbose) as gilmar_mendes:
        
        for prisioneiro in prisioneiros:
            me_liberte(prisioneiro['cela'], 
                        filename=prisioneiro['nome'],
                        verbose=verbose)
