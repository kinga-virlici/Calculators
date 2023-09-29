from Calculators.CalculatorABC import CalculatorABC

class CalculatorSimplu(CalculatorABC):

    def __init__(self):
        super().__init__()

    def adaugare(self, numar):
        self.valoare += numar # self.valoare = self.valoare + numar
        return f'{self.valoare}'

    def scadere(self, numar):
        self.valoare -= numar # self.valoare = self.valoare - numar
        return f'{self.valoare}'

    def inmultire(self, numar):
        self.valoare *= numar # self.valoare = self.valoare * numar
        return f'{self.valoare}'

    def impartire(self, numar):
         if numar != 0:
            self.valoare = self.valoare/numar
            return f'{self.valoare}'
         else:
            print('Operatie invalida: Impartirea la 0 nu este permisa !')


    def calculate(self):
        while True:
            alegere = input('> Alegeti unul dintre aceste simboluri: (+, -, *, /) sau "x" pentru iesire: ')

            if alegere == 'x':
                print('Iesire din calculator')
                break

            if alegere not in ('+', '-', '*', '/'):
                print('Operatie necunoscuta. Alegeti unul dintre aceste simboluri: +, -, *, /')
                continue

            numar = float(input('Introduceti numarul: '))

            if alegere == '+':
                self.adaugare(numar) # daca alegerea este + apelam metoda adaugare
            elif alegere == '-':
                self.scadere(numar)
            elif alegere == '*':
                self.inmultire(numar)
            elif alegere == '/':
                self.impartire(numar)

            self.afisare_rezultat()






