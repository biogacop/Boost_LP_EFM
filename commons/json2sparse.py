#!/usr/bin/python
# Importamos JSON desde BIGG

import urllib,json 
import sys
import os


import argparse

parser = argparse.ArgumentParser(description='Format an csv to homogeneize cols .')
parser.add_argument('--config', action='store', type=str, required=True, help='input config file (reated from "import_model")')
parser.add_argument('--show-inverted', default=False, action='store_true')
#parser.add_argument('--outcsv', action='store', type=str, required=True, help='out csv file')

args = vars(parser.parse_args())


## LEE CONFIGURACION
fconfig = args['config']
with open(fconfig, 'r') as f:
    config = json.load(f)

#datadir = config["datadir"]
datadir = os.path.dirname(fconfig)
SPARSE  = datadir + "/" + config["sparse"]
url = config["url"] 
modo = config["modo"]
#print "URL", url
#print "Nombre objetos", modo 


# DESCARGA E IMPORTACION DE LA MATRIZ

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


file = open(SPARSE,"w") 

if (modo == "numvars"):    
    #Caso en el que la matriz produce la sparse sustituyendo nombres por numeros de reaccion y meta 
    #Estructura para traducir nombres en numeros
    meta_index = {}
    i = 1
    for k in data["metabolites"]:
        meta_index.update({k["id"]: "m"+str(i)})
        i = i+1

    react_index = {}
    i = 1
    for k in data["reactions"]:
        react_index.update({k["id"]: "r"+str(i)})
        i = i+1
    
    for r in data["reactions"]:
        if (r["lower_bound"] <=0) and (r["upper_bound"]<=0): 
            signo = -1
            if (args['show_inverted']): print(r['id'] + " inverted " + str(signo))
        else: signo = 1

        for m in r["metabolites"].keys():
            file.write("%s,%s,%s \n" % (meta_index[m],react_index[r["id"]],signo * r["metabolites"][m]))
else:
    #Caso en el que la matriz produce la sparse con nombres originales
    for r in data["reactions"]:
        if (r["lower_bound"] <=0) and  (r["upper_bound"]<=0) and ((r["lower_bound"] !=0) or  (r["upper_bound"]!=0)): 
            signo = -1
            if (args['show_inverted']): print(r['id'] + " inverted " + str(signo))
        else: 
            signo = 1

        for m in r["metabolites"].keys():
            file.write("%s,%s,%s \n" % (m,r["id"],signo * r["metabolites"][m]))


file.close()

