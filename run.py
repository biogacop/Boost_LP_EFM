#!/usr/bin/python
# -*- coding: utf-8 -*-
#"""
#Created on Mon Jun  3 09:58:26 2019
#
#@author: LEN Y520
#"""

import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.append('./commons/')


import time
import cplex
from cplex.exceptions import CplexError
import numpy as np
import os

import cell
import tools
import lp
from Tableau import *

start = time.time

## Use
# model = 0 for model iAF1260
# model = 1 for model Recon3D
# model = 2 for model iCHOV1
# model = 3 for model e coli core

model=4
numIntentos=1000
reaction=0
scale=0.2
useRLP=True
threshold=10
useRev=True
computeEFM=True

#Arguments to configure the experiment
import argparse

parser = argparse.ArgumentParser(description='Extraction of EFMs using LP')
parser.add_argument('--config', action='store', type=str, required=True, help='Model\'s config file')
parser.add_argument('--loops', action='store', type=int, default = 100, required=False, help='Iterations for the main loop in the experiment')
parser.add_argument('--scale', action='store', type=float, required=True, help='JSON configuring the model and related configs')
parser.add_argument('--reaction', action='store', type=str, default = '', required=False, help='Optional target reaction name (literal)')
parser.add_argument('--disable-RLP', action='store_true', default=False, required=False, help='RLP use (optional)')
parser.add_argument('--threshold', action='store', default=10, required=False, help='Amount of EFMs after Simplex')
parser.add_argument('--disable-compute-efm', action='store_true', default = False, required=False, help='Disable performing EFM verification')
parser.add_argument('--rev', action='store', default = None, type = str, required=False, help='Deterministic index list of reversible reactions ([1,4,6,9])')

args = vars(parser.parse_args())
print("Parameters for the experiment")
print(args)


start=time.time()
experiment(config_model = args['config'], nresults = args['loops'], str_reaction = args['reaction'], scale = args['scale'], useRLP = not args['disable_RLP'], threshold = args['threshold'], computeEFM = not args['disable_compute_efm'], nombreRev = args['rev'])
end=time.time()
print(end-start)

