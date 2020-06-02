
# Importamos JSON desde BIGG

import urllib,json 
import sys


fconfig = sys.argv[1] #"./config_run6.json"
with open(fconfig, 'r') as f:
    config = json.load(f)

url = config["url"]
modo = config["modo"]
#print "URL", url
#print "Nombre objetos", modo 


# DESCARGA E IMPORTACION DE LA MATRIZ
response = urllib.urlopen(url)
data = json.loads(response.read())

#meta_dict =  [item["id"] for item in data["metabolites"]]
#react_dict =  [item["id"] for item in data["reactions"]]


inputs  = []
outputs = []
#Caso en el que la matriz produce la sparse sustituyendo nombres por numeros de reaccion y meta 
#Estructura para traducir nombres en numeros

i = 1
for k in data["reactions"]:
    rr = k["id"]
    if (modo == "numvars"):
        rr = "r"+str(i)
    produce = False
    consume = False
    for m in k["metabolites"]:
        produce = produce or (k["metabolites"][m] > 0)
        consume = consume or (k["metabolites"][m] < 0)
    

    if (produce and not consume):
        inputs.append(rr)
    else:
         if (consume and not produce):
            outputs.append(rr)
        
    i = i+1


print "INPUTS"
for r in inputs:
    print r
print 
print "OUTPUTS"
for r in outputs:
    print r
