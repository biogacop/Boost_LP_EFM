# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 09:58:26 2019

@author: LEN Y520
"""

import time
import sys
import cplex
from cplex.exceptions import CplexError
import numpy as np
import os

import cell
import lp
from Tableau import *

start = time.time()

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

start=time.time()
experiment(numIntentos,model,reaction,scale,useRLP,threshold,computeEFM)
end=time.time()
print(end-start)

