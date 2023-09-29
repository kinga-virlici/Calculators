from abc import ABC, abstractmethod

class CalculatorABC(ABC):

    def __init__(self):
        self.valoare = 0
        print(self.valoare)

    @abstractmethod
    def calculate(self):
        pass

    def afisare_rezultat(self):
        print(f'Rezultatul este {self.valoare}')

    def resetare(self):
        self.valoare = 0
