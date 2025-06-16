import random, constants

class Dices():
    def __init__(self): 
        self.dices = [0] * constants.NUM_DICES #un vector para guardar los valores de los datos

    
    def throw_dices(self):
        for i in range(len(self.dices)):
            self.dices[i] = random.randint(1,6)
        
        print(self.dices)