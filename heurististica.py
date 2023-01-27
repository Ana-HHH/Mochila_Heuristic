import numpy as np
from objetos import Item 

class Heuristica:
    def __init__(self, listaObjetos: list[Item], max_peso:float, max_iter=10000):
        self.listaObjetos = listaObjetos
        self.max_peso = max_peso
        self.max_iter = max_iter

    def RandomValues(self):
        for i in self.listaObjetos:
            if np.random.choice([0,1]) == 1:
                i.OnOff()

    def SumWeight(self):
        pesoTotal = 0
        for i in self.listaObjetos:
            if i.valor == 1:
                pesoTotal += i.peso
        return pesoTotal
    
    def solve(self):
        solucion = [0 for x in self.listaObjetos]
        contador_obj = solucion.count(1)

        iteration_range = self.max_iter 

        for i in range(iteration_range):
            self.RandomValues()
            peso_vecino = self.SumWeight()
            solucion_vecino =  [x.valor for x in self.listaObjetos]
            contador_obj_vecino = solucion_vecino.count(1)

            if contador_obj_vecino > contador_obj and peso_vecino <= self.max_peso :
                solucion, contador_obj = solucion_vecino, contador_obj_vecino

        return (solucion)
