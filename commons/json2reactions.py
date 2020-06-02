
# Importamos JSON desde BIGG

import urllib,json 
import sys
import os

# DESCARGA E IMPORTACION DE LA MATRIZ


fconfig = sys.argv[1] #"./config_run6.json"
with open(fconfig, 'r') as f:
    config = json.load(f)

url = config["url"]
modo = config["modo"]

datadir = os.path.dirname(fconfig)
filename = datadir + "/" + url.split("/")[-1] 
if not (os.path.isfile(filename)):
    response = urllib.urlopen(url)
    data = json.loads(response.read())
else:
    with open(filename) as json_file:
        data = json.load(json_file)

#meta_dict =  [item["id"] for item in data["metabolites"]]
#react_dict =  [item["id"] for item in data["reactions"]]

if (modo == "numvars"):    
    #Caso en el que la matriz produce la sparse sustituyendo nombres por numeros de reaccion y meta 
    #Estructura para traducir nombres en numeros

    react_index = {}
    i = 1
    for k in data["reactions"]:
        print("r"+str(i))
        i = i+1
else:
    #Caso en el que la matriz produce la sparse con nombres originales
    for k in data["reactions"]:
        print(k["id"]) #, k["lower_bound"], k["upper_bound"]

