


# DESCARGA E IMPORTACION DE LA MATRIZ




import numpy as np
import csv
import sys
import os

sys.path.append("../comunes/utiles.py")
from utiles import Tools



class Cell:

    #Partimos de la matriz sparse y las reacciones reversibles se desdoblan si se indican
    def __init__(self, SPARSE, REV = '', BLOCKED = ''):
        self.S          = np.zeros(2)
        self.METAS      = set([])
        self.asocMETAS  = {}
        self.REACT      = set([])
        self.asocREACT  = {} 
        self.lMETAS     = []
        self.lREACT     = []

        self.nREACT     = 0
        self.nMETAS     = 0

        self.INPUTS     = set([])   #Conjunto de reacciones de salida
        self.OUTPUTS    = set([])   #Conjunto de reacciones de entrada

        self.REV       = set([])

        self.BLOCKED    = set([])   #Reacciones bloqueadas

        sufijo          = '_rev'

        #Esperamos que el fichero de reversibles sea una lista con una por linea o csv donde interesa la primera col
        if (REV!='' and os.path.isfile(REV)):
            with open(REV, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    self.REV.add(row[0])

        #Esperamos que el fichero de reversibles sea una lista con una por linea o csv donde interesa la primera col
        if (BLOCKED!='' and os.path.isfile(BLOCKED)):
            with open(BLOCKED, 'rt') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for row in reader:
                    self.BLOCKED.add(row[0])

        #Revisamos la sparse para obtener reacciones y metabolitos
        with open(SPARSE, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                if (not row[0] in self.METAS):
                    self.asocMETAS[row[0]] = len(self.asocMETAS)
                    self.METAS.add(row[0])
                    self.lMETAS.append(row[0])

                if (not row[1] in self.REACT):
                    self.asocREACT[row[1]] = len(self.asocREACT)
                    self.REACT.add(row[1])
                    self.lREACT.append(row[1])
                    self.INPUTS.add(row[1])         #Candidato a ser de input
                    self.OUTPUTS.add(row[1])        # .. y candidato a ser de output
                    if (row[1] in self.REV):
                        re = row[1]+sufijo
                        self.asocREACT[re] = len(self.asocREACT)
                        self.REACT.add(re)
                        self.lREACT.append(re)
                        self.INPUTS.add(re)         #Candidato a ser de input
                        self.OUTPUTS.add(re)        # .. y candidato a ser de output
                        

        #En una segunda pasada creamos la matriz
        self.S = np.zeros(len(self.METAS) * len(self.REACT)).reshape(len(self.METAS), len(self.REACT))
        with open(SPARSE, 'rt') as csvfile:
            reader = csv.reader(csvfile, delimiter=',')
            for row in reader:
                self.S[self.asocMETAS[row[0]]][self.asocREACT[row[1]]] = float(row[2])
                
                if (row[1] in self.REV):
                    re = row[1]+sufijo
                    self.S[self.asocMETAS[row[0]]][self.asocREACT[re]] = float(row[2]) * -1
        
        #Busca entradas y salidas
        for m in self.lMETAS:
            for r in self.lREACT:
                st = self.S[self.asocMETAS[m]][self.asocREACT[r]]
                if (st > 0):
                    if (r in self.OUTPUTS):
                        self.OUTPUTS.remove(r) # No es reaccion de salida si consume
                else:
                    if (st < 0):
                        if (r in self.INPUTS):
                            self.INPUTS.remove(r) # No es reaccion de entrada si pruce
                    
            
        

        self.nREACT = len(self.REACT)
        self.nMETAS = len(self.METAS)

        self.Slist =  np.matrix(np.transpose(self.S)).tolist()
        #self.Slist =  np.matrix(self.S).tolist()

    #Dado el vector soporte de una solucion, se devuelve la submatriz
    def subproblem(self, _supp):
        T = Tools()
        return self.S[:,T.Vector2pos(_supp)]


    def digraph(self):
        dg = []
        for m in self.lMETAS:
            for r in self.lREACT:
                st = self.S[self.asocMETAS[m]][self.asocREACT[r]]
                if (st > 0):
                    dg.append([r,m,1])
                else:
                    if (st < 0):
                        dg.append([m,r,1])
        return dg

    #Nos quedamos solo con las reacciones
    def supp(self,efm):
        efm = self.reacts_assoc(efm)
        r = []
        for i in range(self.nREACT):
            if (i in efm):
                r.append(1)
            else:
                r.append(0)
        return r

    #Nos quedamos solo con las reacciones
    def reacts(self,efm):
        return [x for x in efm if x in self.REACT]

    #Nos quedamos solo con las posiciones de las reacciones dentro de la lista
    #Es util por que puede usarse como semilla en LP
    def reacts_assoc(self,efm):
        return [self.asocREACT[x] for x in efm if x in self.REACT]
                    
            
    

if __name__ == '__main__':
    import json 
    import sys

    print ("Ejecutando Cell.py en modo script")

    fconfig = "../basico/config_example.json"
    with open(fconfig, 'r') as f:
        config = json.load(f)

    datadir = config["datadir"] 
    SPARSE  = datadir + config["sparse"] 
    REV     = datadir + config["reversibles"] 
    C = Cell(SPARSE)
    print (C.S)
    print (np.transpose(C.S))

    print(C.reacts(['r1','m1','r2']))
    print( C.reacts_assoc(['r1','m1','r2']))
    print( C.supp(['r1','m1','r2']))

#print METAS
#print asocMETAS
#print REACT
#print asocREACT
#print
#print 'accoa_c', S[asocMETAS['accoa_c']]



