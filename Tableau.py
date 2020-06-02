#-*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:58:26 2019

@author: LEN Y520
"""

import cplex
from cplex.exceptions import CplexError
import numpy as np
import os
import sys


sys.path.append("../commons")
from cell import Cell
from lp import *
import time
import random 
import json

                 
def calculateSupport(P,e=0):
    sop=[]
    for j in range(len(P)):
        if P[j]>e:
            sop.append(j)
    return sop


def writeFile(myList,name,output_dir = "./output/"):
    if name=="":
        for i in range(1000):
            tempName= output_dir + "EFMs"+str(i)+".txt"
            if not (os.path.isfile(tempName)):
                name=tempName
                break

    else:
        name = output_dir + name + ".txt"
    myFile=open(name,"w+")
    myFile.write(str(myList))    
 

def chooseF(n,lista,escala):
    f1=[]
    f2=[]
    num=int(round(len(lista)*escala))
    lis=range(len(lista))
    
    dif=np.random.choice(lis, size=num, replace=False, p=None)
    for j in dif:
        f1.append(lista[int(j)])
        f2.append(-1+2*np.random.rand() )
    return [f1,f2,dif]
    
                 
def experiment(config_model, nresults = 1, str_reaction='', scale=0.2, useRLP=True, threshold=4, computeEFM=False, nombreRev=None):

    print(config_model)
    with open(config_model, 'r') as f:
        config = json.load(f)
       
    datadir = os.path.dirname(config_model) + "/"
    SPARSE  = datadir + config["sparse"]
    REV     = datadir + config["reversibles"]
    C = Cell(SPARSE,REV)   
    C.removeMetab(C.externalMetab());
    
    solver = LPCplex()
    
    _cols = solver.matrix2columns(C.Slist)
    solver.populate_by_column(_cols, [0] * C.nMETAS, [1] * C.nREACT, ['E'] * C.nMETAS, 'minimize', C.lREACT)
    if (str_reaction != ''):
        reaction = C.assocREACT[str_reaction]
        solver.add_constraint([C.lREACT[reaction]],[1],1,"E",_name="r1")
    else:
        reaction = -1


    noRev=[]
    rev= []
    if nombreRev:
        ficheroRev=open(nombreRev,"r")
        listaRev=eval(ficheroRev.read())
        for k in listaRev:
            rev.append(int(k))
        for k in range(C.nREACT):
            if not k in rev:
                noRev.append(k)    
    else:
        rev = C.asocfullREV
        noRev = list (set(range(C.nREACT)) - set(rev))
    
    soportes=[]
    print("nresults %d" % nresults)
    
    cont0=0
    cont1=0
    
    start=time.time()
    
    for j in range(nresults):
        solver.problem.parameters.simplex.limits.iterations=10**14
        if len(soportes)>nresults:
        
            break

        funcion=chooseF(C.nREACT,noRev,scale)
        solver.setF(funcion[0],funcion[1],C.nREACT)   
        if reaction<0:
            number=random.choice(range(2,len(noRev)))
            reaccion=random.sample(noRev,number)
            valor=[]
            for r in reaccion:
              valor.append(np.random.rand())
            solver.add_constraint(reaccion,valor,1,"E","r1")
            
        else:
            solver.add_constraint([reaccion],[1],1,"E","r1")
        
        solver.solve("")
        cont0+=1
        sol=solver.sol_vars() 
        
        if len(sol)>0:
            basis=solver.problem.solution.basis.get_basis()
            sop=calculateSupport(sol,10**-14)
            if len(sop)==2:
                for R in sop:
                    if not R in rev:
                        rev.append(R)
                        
            else:
                if not sop in soportes:
                    soportes.append(sop)
                    #print("EFMS %d " % len(soportes))
                    solver.problem.start.set_start(col_status=basis[0],row_status=basis[1],col_primal=sol,row_primal=[],col_dual=[],row_dual=[])
                    if useRLP:
                        solver.problem.parameters.simplex.limits.iterations=random.choice(range(1,5))
                        contador=1
                        while contador<threshold and len(soportes)<=nresults:
                            escala2=0.2
                            funcion=chooseF(C.nREACT,noRev,escala2)
                            solver.setF(funcion[0],funcion[1],C.nREACT)   
                            solver.solve("")
                            cont1+=1
                            sol2=solver.sol_vars()
                            sop2=calculateSupport(sol2,10**-14)   
                            if not sop2 in soportes:
                                soportes.append(sop2)
                                #print("inner EFMS %d " % len(soportes))
                                contador=0
                            else:
                                contador+=1 
    
    print("Number of EFMs found",len(soportes))
    print("Number of solved LPs",cont0)
    print("Number of solved RLPs",cont1)
    if computeEFM:
        writeFile(soportes,"")


       

