#!/usr/bin/python


# DESCARGA E IMPORTACION DE LA MATRIZ




import numpy as np
import csv
import sys
import os

sys.path.append("./commons")
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

        self.REV       = set([])    #Imported from a file
        self.fullREV   = []         #Built from REV with respective pairs. Full list
        self.asocfullREV   = []     #Built from REV with respective pairs. Full list of indexes
        
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
                        #List of reversible reactions
                        self.fullREV.append(row[1])
                        self.asocfullREV.append(self.asocREACT[row[1]])
                        self.fullREV.append(re)
                        self.asocfullREV.append(self.asocREACT[re])
                        
                        

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

    #External metabolites detection
    def externalMetab(self):
        externals = []
        for m in self.lMETAS:
            signo = 0
            external = True
            for r in self.lREACT:
                st = self.S[self.asocMETAS[m]][self.asocREACT[r]]
                if (external and (st!=0)):
                    if (signo == 0):
                        if (st<0): signo = -1
                        else: signo = 1
                    else:
                        if (st != 0):
                                external = ((signo == -1) and (st<0)) or ((signo == 1) and (st>0))
            if external: externals.append(m)
        return externals

    #Generic consistent removel of  metabolites
    #Applied to remove external metabolites. See externalMetab()
    # @@listm, list of metabolites named by its literal
    def removeMetab(self, listm):

        #Firstly, cleaning up the metabolites
        for m in listm:
            asoc = self.asocMETAS[m]
            self.S = np.delete(self.S,asoc,0)
            del self.asocMETAS[m]
            #Asociative dict needs to be updated
            for k in self.asocMETAS:
                if asoc < self.asocMETAS[k]:
                   self.asocMETAS[k] -=1

            self.lMETAS.remove(m)
            self.METAS.remove(m)


        #Secondly, removing unused reactions in any equation
        #Detection
        toremove = []
        for r in self.lREACT:
            useful = False
            for m in self.lMETAS:
                useful = useful or (self.S[self.asocMETAS[m]][self.asocREACT[r]] != 0)
            if (not useful): toremove.append(r) 
        #Removing 
        for r in toremove:
            asoc = self.asocREACT[r]
            self.S = np.delete(self.S,asoc,1)
            del self.asocREACT[r]
            #Asociative dict needs to be updated
            for k in self.asocREACT:
                if asoc < self.asocREACT[k]:
                   self.asocREACT[k] -=1

            self.lREACT.remove(r)
            self.REACT.remove(r)
    
        #Coherencia a variables calculadas
        self.nMETAS = len(self.lMETAS)
        self.nREACT = len(self.lREACT)
        self.Slist =  np.matrix(np.transpose(self.S)).tolist()
            
        
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

    print ("Running cell.py en modo script")

    datadir = "../models/toymodel/"
    fconfig = datadir + "config_toymodel.json" 
    print (fconfig)
    with open(fconfig, 'r') as f:
        config = json.load(f)

    SPARSE  = datadir + config["sparse"] 
    REV     = datadir + config["reversibles"] 
    C = Cell(SPARSE)
    print("\n Stoichiometric matrix S")
    print (C.S)
    print("\n Transposed S")
    print (np.transpose(C.S))

    e = ['r1','m1','r2']
    print("\n Support of " + ",".join(e))
    print( C.supp(e))

    print("\n Flux (only reacts) " + ",".join(e))
    print(C.reacts(e))

    print("\n Submatrix of S corresponding to flux e = " + ",".join(e))
    print(C.subproblem(C.supp(e)))

    print("\n External metabolites in S") 
    print(C.externalMetab())
    #print( C.reacts_assoc(e))

    #After remove external metabolites
    C.removeMetab(C.externalMetab());
    print("\n Stoichiometric matrix S")
    print (C.S)

 
    datadir = "../models/e_coli_core/" 
    fconfig = datadir + "config_e_coli_core.json"
    print("\n " + fconfig)
    with open(fconfig, 'r') as f:
        config = json.load(f)

    SPARSE  = datadir + config["sparse"] 
    REV     = datadir + config["reversibles"] 
    C = Cell(SPARSE,REV)
    print("\nReactions = %d" % C.nREACT)
    print("\n External metabolites in S") 
    print(C.externalMetab())

    print("\n Reversible reactions in S") 
    print(C.fullREV)
    print(C.asocfullREV)


