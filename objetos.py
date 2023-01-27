class Item:
    def __init__(self, nombre, id, peso, valor=0):
        self.nombre = nombre
        self.id = id
        self.peso = peso
        self.valor = valor         

    def OnOff(self):
        self.valor = 1 if self.valor == 0 else 0

