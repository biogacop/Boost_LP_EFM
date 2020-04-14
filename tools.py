


# DESCARGA E IMPORTACION DE LA MATRIZ




import numpy as np
import csv


class Tools:

    #Soporte de un vector
    def supp(self, _vector, _umbral):
        v = []
        for i in _vector:
            if (i>_umbral):
                v.append(1)
            else:
                v.append(0)

            
        return v

    #VEctor random del numero de dimensiones o su soporte
    def rndVector(self, _dim, _supp):
        v = np.random.rand(_dim)
        if (_supp):
            return self.supp(v,0.5)
        return v

    #Dado un vector con 0 y 1's devuelve las posiciones donde hay 1's
    def Vector2pos(self,v):
        return [i for i in range(len(v)) if v[i]==1]


    #Sacar las columnas de la matriz densa, una por cada fila
    def matrix2columns(self, _matrix):
        num_v = len(_matrix[0])
        m = []
        for i in range(len(_matrix)):
            l = [range(num_v)]
            l.append(_matrix[i])
            m.append(l)
        return m
        


if __name__ == '__main__':
    import sys

    print ("Ejecutando Cell.py en modo script")

    T = Tools()
    #Vector y soporte en uno
    v = T.rndVector(10, True)
    print(v)

    
    #Vector simple
    v = T.rndVector(10, False)
    print(v)
    #Ahora el soporte
    print(T.supp(v,0.5))
    #Posiciones
    print(T.Vector2pos(T.supp(v,0.5)))



