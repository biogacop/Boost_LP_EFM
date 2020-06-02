#!/usr/bin/python
# ---------------------------------------------------------------------------
"""
Imports a model and produces a numpy's format dense matrix

"""

#from __future__ import print_function

_digrafo = False

import numpy 
import json
import sys
import os

#sys.path.append("../comunes/")
from cell import Cell
from utiles import Tools

import argparse

parser = argparse.ArgumentParser(description='Format an csv to homogeneize cols .')
parser.add_argument('--config', action='store', type=str, required=True, help='input config file (reated from "import_model")')
parser.add_argument('--verbose', default=False, action='store_true')
#parser.add_argument('--outcsv', action='store', type=str, required=True, help='out csv file')

args = vars(parser.parse_args())


## LEE CONFIGURACION
fconfig = args['config']
with open(fconfig, 'r') as f:
    config = json.load(f)

datadir = os.path.dirname(fconfig)
SPARSE  = datadir + "/" + config["sparse"]
REV     = datadir + "/" + config["reversibles"]
m_file  = datadir + "/" + config["matrix_file"]


C = Cell(SPARSE, REV) 
if (args['verbose']):
    print("#reacciones = ", C.nREACT);
    print("reacciones = ", C.lREACT);
    print("metabolitos = ", C.lMETAS);
    print("reversibles = ", C.REV);
    print("metas = ", C.nMETAS);
    print("Reacciones de entrada = " , C.INPUTS)
    print("Reacciones de salida = ", C.OUTPUTS)

    cols = [1]* C.nREACT
    print(C.subproblem(cols))
    print(C.S)

#numpy.savetxt(m_file, numpy.transpose(C.S), delimiter = ' ') 
numpy.savetxt(m_file, C.S, delimiter = ' ') 

if (args['verbose']):
    print("Generado  " + m_file)


