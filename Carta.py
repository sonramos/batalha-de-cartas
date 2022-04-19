class Carta:
    NAIPE = ["\u2666", "\u2660", "\u2663", "\u2665"] # Ouro, Espadas, Paus, Copas
    NUMERO = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    def __init__(self, numero, naipe):
        self.__numero = numero
        self.__naipe = naipe

    @property
    def naipe(self):
        return self.__naipe

    @property
    def numero(self):
        return self.__numero

    def __lt__(self, other):
        return self.__numero < other.__numero
    
    def __str__(self): # todas as informacoes da carta
        return f'{Carta.NUMERO[self.__numero]}{Carta.NAIPE[self.__naipe]}'
