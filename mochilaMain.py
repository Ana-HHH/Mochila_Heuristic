import numpy as np
from matplotlib import pyplot
from objetos import Item 
from heurististica import Heuristica

## Definiendo la mochila y los objetos
pesoMaxMochila = 4.5

obj1 = Item('obj1', id=1, peso=1.5)
obj2 = Item('obj2', id=2, peso=2.0)
obj3 = Item('obj3', id=3, peso=0.5)
obj4 = Item('obj4', id=4, peso=4.5)
obj5 = Item('obj5', id=5, peso=1.0)
obj6 = Item('obj6', id=1, peso=0.2)
obj7 = Item('obj7', id=1, peso=0.3)

lista = [obj1, obj2, obj3, obj4, obj5, obj6, obj7]

solver = Heuristica(lista, pesoMaxMochila)

print(solver.solve())