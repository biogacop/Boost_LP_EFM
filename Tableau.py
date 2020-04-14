# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:58:26 2019

@author: LEN Y520
"""

import cplex
from cplex.exceptions import CplexError
import numpy as np
import os

from lp import *
import cell
import time
import random 

                 
def miSoporteError(P,e=0):
    sop=[]
    for j in range(len(P)):
        if P[j]>e:
            sop.append(j)
    return sop


def escribe(lista,nombreF):
    if nombreF=="":
        for i in range(1000):
            nombre="./datos/EFMs"+str(i)+".txt"
            if not (os.path.isfile(nombre)):
                nombreCS=nombre
                break

    else:
        nombre="./datos/"+nombreF+".txt"
    fichero=open(nombre,"w+")
    fichero.write(str(lista))    
    
 
def elegirF2(n,escala):
    f1=range(n)
    f2=np.zeros(n)
    num=int(round(n*escala))
    dif=np.random.randint(0,n-1,num)
    for j in dif:
       f2[int(j)]=6*np.random.rand()  
    return [f1,f2,dif]


def elegirF3(n,lista,escala):
    f1=[]
    f2=[]
    num=int(round(len(lista)*escala))
    lis=range(len(lista))
    
    dif=np.random.choice(lis, size=num, replace=False, p=None)
    for j in dif:
        f1.append(lista[int(j)])
        f2.append(6*np.random.rand() )
    return [f1,f2,dif]
 
            
def experiment(num,model=0,reaction=0,scale=0.2,useRLP=True,threshold=4,computeEFM=False):
    import json
    import sys
    sys.path.append("../comunes/cell.py")
    from cell import Cell

    if model==0:
        fconfig = "./config_iAF1260.json"
        fin="iAF"
        eff=0.1089653
        scale=0.17
        nombreRev="./datos/reviAF.txt"
    if model==1:
        fconfig = "./config_Recon3D.json"
        fin="Rec"
        scale=0.88
        nombreRev="./datos/revRec.txt"
        eff=0.1284078
    if model==2:
        fconfig = "./config_iCHOv1.json"
        fin="iCHO"
        scale=0.8
        nombreRev="./datos/reviCHO.txt"
        eff=0.05800386
    if model==3:
        fconfig="./config_e_coli_core.json"    
        fin="Core"
        scale=0.2
        nombreRev="./datos/reveColi.txt"
        eff=0.2
    with open(fconfig, 'r') as f:
        config = json.load(f)
        
        
    datadir = config["datadir"]
    SPARSE  = datadir + config["sparse"]
    REV     = datadir + config["reversibles"]
    C = Cell(SPARSE,REV)   
    solver = LPCplex()
    _cols = solver.matrix2columns(C.Slist)
    solver.populate_by_column(_cols, [0] * C.nMETAS, [1] * C.nREACT, ['E'] * C.nMETAS, 'minimize', C.lREACT)
    solver.add_constraint([C.lREACT[reaction]],[1],1,"E",_name="r1")
    solver.lpfile("test.lp")

    noRev=[]
    ficheroRev=open(nombreRev,"r")
    listaRev=eval(ficheroRev.read())
    rev=[]
    for k in listaRev:
        rev.append(int(k))
    for k in range(C.nREACT):
        if not k in rev:
            noRev.append(k)    
    
    soportes=[]
    for j in range(num):
        solver.problem.parameters.simplex.limits.iterations=10**14
        if len(soportes)>num:
            break
        funcion=elegirF2(C.nREACT,scale)
        solver.setF(funcion[0],funcion[1],C.nREACT)   
        if reaction==0:
            try:
              solver.del_constraint("r1")
            except:
              pass
            reaccion=noRev[int(np.random.randint(0,len(noRev),1))]
        solver.add_constraint([reaccion],[1],1,"E","r1")
        solver.solve("")
        sol=solver.sols()   
        if len(sol)>0:
            sop=miSoporteError(sol,10**-14)
            if len(sop)==2:
                for R in sop:
                    if not R in rev:
                        rev.append(R)
            else:
                if not sop in soportes:
                    soportes.append(sop)
                    solver.problem.start.set_start(col_status=[],row_status=[],col_primal=sol,row_primal=[],col_dual=[],row_dual=[])
                    if useRLP:
                        solver.problem.parameters.simplex.limits.iterations=1
                        contador=1
                        while contador<threshold and len(soportes)<=num:
                            escala2=0.2
                            funcion=elegirF3(C.nREACT,sop,escala2)
                            solver.setF(funcion[0],funcion[1],C.nREACT)   
                            solver.solve("")
                            sol2=solver.sols()
                            sop2=miSoporteError(sol2,10**-14)   
                            if not sop2 in soportes:
                                soportes.append(sop2)
                                contador=0
                            else:
                                contador+=1 
    if computeEFM:
        escribe(soportes,"")


       

