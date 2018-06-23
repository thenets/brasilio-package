import rows
import os
from timeit import default_timer
import json

output_path = '../package/data/'

class Brasilio(object):
    def __init__(self, output_path='../package/data/', verbose=False):
        self.verbose = verbose
        self.output_path = output_path
        self.timer = default_timer
        
    def __enter__(self):
        
        # Cria diretório package 
        if not os.path.exists(self.output_path):
            os.makedirs(self.output_path)
        
        # Cria resouces.py vazio
        json.dump([], open("resources.json", "w"), indent=2)
        
        # Start Timer
        self.start = self.timer()
        
        return self
        
    def __exit__(self, *args):
        
        # Cria datapackage
        create_datapackage(self.output_path, verbose=False)

        # End Timer
        end = self.timer()
        self.elapsed_secs = end - self.start
        self.elapsed = self.elapsed_secs  # millisecs
        if self.verbose:
            print('Sucesso!\n Sua captura demorou: {0:.2f} s'.format(self.elapsed))


def generate_resources(filename, verbose=False):

    data_path = os.path.join(output_path, filename)

    if verbose: 
        print('Reading Data')

    data = rows.import_from_csv(data_path)

    translate = {int: 'integer',
                str: 'string'}

    resource = {'format': "csv",
                "url": "http://brasil.io/dataset/{}?format=csv".format(filename.split('.')[0]),
                "path": data_path,
                "profile": "tabular-data-resource",
                'schema': {
                'fields': []}
                }

    for i, field in enumerate(data.field_names):
        
        resource['schema']['fields'].append({'name': field,
                                            'type': translate[data.field_types[i].TYPE[0]]})

    if verbose: 
        print('Writing resources.json')
        # print(type(resources))
        # print(json.dumps(resources))
    

    resources = json.load(open("resources.json", "r"))
    resources.append(resource)
    json.dump(resources, open("resources.json", "w"), indent=2)


def create_datapackage(output_path, verbose=False):

    # Criar o datapackage.json
    if verbose:
        print("Criando datapackage.json")
   
    with open("metadata.json", "r") as mfd:
        output = json.load(mfd)

        with open("resources.json", "r") as rfd:
            output['resources'] = json.load(rfd)
        
        with open("../package/datapackage.json", "w") as datapackage:
            json.dump(output, datapackage, indent=2)

if __name__ == '__main__':
    pass