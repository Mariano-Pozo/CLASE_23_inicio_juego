import json
def data_json(nombre_archivo:str):
    lista= []
    with open(nombre_archivo, "r") as archivo:
        dict = json.load(archivo)
        lista = dict
    return lista