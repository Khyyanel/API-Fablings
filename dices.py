import random, constants

class Dices():
    def __init__(self, quantity): 
        self.dices = [0] * quantity 
        #La cantidad de dados es un parámetro en la función
        #Inicializamos todos los dados en cero. [0] es un vector o una lista de ceros
        
    def throw_dices(self):
        for num in range(len(self.dices)): 
            self.dices[num] = random.randint(1,6)
        
        print(self.dices)

        #por cada número en el rango de la longitud de los dados, le asignamos un número random, es decir, 
        #a cada dado en la lista self.dices dale un número random del 1 al 6