from Baralho import Baralho
from PilhaEncadeada import Pilha

class Player:
    ID = 0
    def __init__(self):
        Player.ID += 1
        self.__name = ''
        self.__id = Player.ID
        self.__win = 0
        self.mao = Pilha()
        
    #get name
    @property
    def name(self):
        return self.__name

    #get id
    @property
    def id(self):
        return self.__id

    #get win
    @property
    def win(self):
        return self.__win

    #set name        
    @name.setter
    def name(self, name):
        self.__name += name
    
    #set win
    @win.setter
    def win(self, value):
        self.__win = value
    

    def __str__(self):
        return f'Jogador {self.id}: {self.name}'