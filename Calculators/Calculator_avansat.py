from Calculators.CalculatorABC import CalculatorABC
import math

class CalculatorAvansat(CalculatorABC):

    def __init__(self):
        super().__init__()

    def modulo(self, numar1, numar2): # avem nevoie de 2 parametri pentru impartire;
        self.valoare = numar1 % numar2 # returneaza restul impartirii
        return f'{self.valoare}'

    def exponential(self, numar, putere): # avem nevoie de 2 parametri: baza si puterea
        self.valoare = numar ** putere # poate fi utilizata si functia pow()
        return f'{self.valoare}'

    def logaritm(self, numar):
        self.valoare = math.log(numar)
        return f'{self.valoare}'

    def radical(self, numar):
        self.valoare = math.sqrt(numar)
        return f'{self.valoare}'

    def calculate(self):

        while True:
            alegere = input('> Selectati operatia dorita: (%, pow, log, rad): \n ')

            if alegere == 'x':
                print('Iesire din calculator')
                break

            if alegere not in ('%', 'pow', 'log', 'rad'):
                print('Operatie necunoscuta. Alegeti unul dintre aceste simboluri: %, pow, log, rad')
                continue

            numar = float(input('Introduceti numarul: '))

            if alegere in ('%', 'pow'): # daca alegerea este modulo sau exponential avem nevoie de 2 numere
                numar2 = float(input('Introduceti al doilea numar: '))

            if alegere == '%':
                self.modulo(numar, numar2)
            elif alegere == 'pow':
                self.exponential(numar, numar2)
            elif alegere == 'log':
                self.logaritm(numar)
            elif alegere == 'rad':
                self.radical(numar)

            self.afisare_rezultat()
            self.resetare() # avem nevoie de o functie care sa reseteze calculatorul avansat dupa fiecare op.


