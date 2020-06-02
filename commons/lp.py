#!/usr/bin/python
# ---------------------------------------------------------------------------
"""
Illustrating the CPLEX callback functionality.
"""

from __future__ import print_function

import os
import cplex
class LPCplex:

    def __init__(self):
        self.problem = cplex.Cplex()


    def matrix2columns(self, _matrix):
        num_v = len(_matrix[0])
        m = []
        for i in range(len(_matrix)):
            l = [range(num_v)]
            l.append(_matrix[i])
            m.append(l)
        return m

    #Genera el problema
    #cols, la matriz S traspuesta
    #rhs,    vector b  (Cx = b), minimizando es (0)
    #obj,    coeficientes de F
    #senses, vector de igualdades de las ecuaciones
    #sense,  sentido de la funcion
    def populate_by_column(self, _cols, _rhs, _obj, _senses, _sense, _names):
        self.problem.linear_constraints.add(rhs=_rhs, senses= _senses)

        if (_sense == 'maximize'):
            self.problem.objective.set_sense(self.problem.objective.sense.maximize)
            #Imcompleto: no tengo claro los limites maximizando
            #Cargamos los coeficientes
            #self.problem.variables.add(obj=_obj, columns=_cols, -b = [-1 * cplex.infinity]*len(_obj), ub=[0]*len(_obj))
        else: 
            self.problem.objective.set_sense(self.problem.objective.sense.minimize)
            #Cargamos los coeficientes
            #self.problem.variables.add(names = _names, obj=_obj, columns=_cols, ub = [cplex.infinity]*len(_obj), lb=[0]*len(_obj))
            self.problem.variables.add(names = _names, obj=_obj, columns=_cols, ub = [cplex.infinity]*len(_obj), lb=[0]*len(_obj))

    #Permite modificar la funcion objetivo reaprovechando el resto del LP
    def setF(self,  _vars, _coef, n): #_vars, _coef):
        #La formula abreviada me da un error ....
        #self.problem.objective.set_linear([cplex.SparsePair(ind=_vars, val= _obj)])

        # ... por eso la dejo menos eficiente
        for i in range(len(_vars)):
            self.problem.objective.set_linear(_vars[i], _coef[i])
    

    #Add restricciones adicionales
    def add_constraint(self, _vars, _coef, _rhs, _senses, _name = 'addcons'):
        self.problem.linear_constraints.add(lin_expr = [cplex.SparsePair(ind=_vars, val=_coef)], rhs = [1.0], senses=["E"], names = [_name])
      
    def del_constraint(self, _name):
        self.problem.linear_constraints.delete(_name)
 
    #Guarda la formulacion del LP en un fichero 
    def lpfile(self,f):
        self.problem.write(f);
       
    #Resuelve el problema y eventualmente se puede indicar un fichero para log 
    def solve(self,cplexlog = ''):
        if (cplexlog==''):
            cplexlog = None
        
        self.problem.set_results_stream(cplexlog)
        self.problem.set_warning_stream(cplexlog)
        self.problem.set_error_stream(cplexlog)
        self.problem.set_log_stream(cplexlog)

        self.problem.parameters.lpmethod.set(self.problem.parameters.lpmethod.values.primal)

        self.problem.solve()

    #Muestra la solucion
    def sols(self):
        solution = self.problem.solution

        # the following line prints the corresponding string
        print(solution.status[solution.get_status()])
        print("Objective value = ", solution.get_objective_value())
        print()
        numvars = self.problem.variables.get_num()
        numlinconstr = self.problem.linear_constraints.get_num()
        print("Values          = ", solution.get_values(0, numvars - 1))
        print("Slacks          = ",
        solution.get_linear_slacks(0, numlinconstr - 1))
        print("Duals           = ",
        solution.get_dual_values(0, numlinconstr - 1))
        print("Reduced Costs   = ", solution.get_reduced_costs(0, numvars - 1))

    #Vector solucion
    def sol_vars(self):
        numvars = self.problem.variables.get_num()
        try:
            return self.problem.solution.get_values()
        except:
            return []
    #Valor de la funcion objetivo
    def sol_obj(self):
        return self.problem.solution.get_objective_value()

    #Coeficientes de la funcion objetivo
    def f(self):
        return self.problem.objective.get_linear()


if __name__ == "__main__":
    import json
    import sys

    sys.path.append("../comunes/cell.py")
    from cell import Cell

    print("Test del solver cplex y cell en modo script")

    fconfig = "../models/toymodel/config_toymodel.json"
    with open(fconfig, 'r') as f:
        config = json.load(f)

    datadir = os.path.dirname(fconfig) + "/"
    SPARSE  = datadir + config["sparse"]
    REV     = datadir + config["reversibles"]
    C = Cell(SPARSE, REV) 
    print("reacciones = ", C.nREACT);
    print("metas = ", C.nMETAS);
    C.removeMetab(C.externalMetab());

    ##import numpy
    solver = LPCplex()
    _cols = solver.matrix2columns(C.Slist)
    print ("len(_cols) =  %d, nMETAS = %d, nREACT = %d, len(lREACT) = %d" % (len(_cols), C.nMETAS, C.nREACT, len(C.lREACT)))
    solver.populate_by_column(_cols, [0] * C.nMETAS, [1] * C.nREACT, ['E'] * C.nMETAS, 'minimize', C.lREACT)
    #Solo una variable y su coeficiente
    solver.add_constraint(['r1'],[1],1,"E")
    #Varias variables y sus coeficientes
    solver.add_constraint(['r3','r4'],[1,0],1,"E")
    #Todas las variables y sus coeficientes
#    solver.add_constraint(C.lREACT,[0,0,0,1,0,0,0],1,"E")
    solver.lpfile("test.lp")
    solver.solve("test.log")
    solver.sols()

