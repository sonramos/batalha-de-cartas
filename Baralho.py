# Baralho = coleçao de cartas (lista de cartas)
from Carta import Carta
import random

class BaralhoException(Exception):
    def __init__(self, msg):
        super().__init__(msg)

class Baralho:
    def __init__(self):
        self.baralho = list()
        for naipe in range(4):
            for numero in range(13):
                self.baralho.append( Carta(numero, naipe))
        # Inicia baralho já embaralhado
        self.embaralhar()

    def __len__(self):
        return len(self.baralho)

    def temCarta(self):
        if len(self.baralho) > 0:
            return True
        else:
            return False
    
    def retirarCarta(self)->Carta:
        try:
            return self.baralho.pop()
        except IndexError :
            raise BaralhoException('O baralho está vazio. Não há cartas para retirar')
            
    def embaralhar(self):
        random.shuffle(self.baralho)

    def __str__(self):
        saida = ''
        for carta in self.baralho:
            saida += carta.__str__() + '\n' 
        return saida
