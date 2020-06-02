
# Importamos JSON desde BIGG

import urllib,json 
import sys
import os


import argparse

parser = argparse.ArgumentParser(description='Format an csv to homogeneize cols .')
parser.add_argument('--config', action='store', type=str, required=True, help='input config file (reated from "import_model")')

args = vars(parser.parse_args())

## LEE CONFIGURACION
fconfig = args['config']
with open(fconfig, 'r') as f:
    config = json.load(f)

#datadir = config["datadir"]
datadir = os.path.dirname(fconfig)
reversibles = datadir + "/" + config["reversibles"]
url = config["url"]
modo = config["modo"]


# DESCARGA E IMPORTACION DE LA MATRIZ
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

file = open(reversibles,"w")

i = 1
for k in data["reactions"]:
    rr = k["id"]
    if (modo == "numvars"):
        rr = "r"+str(i)
    es = False
    for m in k["metabolites"]:
        es = es or (k["lower_bound"] * k["upper_bound"]<0)

    if (es):
        file.write(rr + "\n")
    i = i+1


