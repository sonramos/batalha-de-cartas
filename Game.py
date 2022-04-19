from Player import Player
from Baralho import Baralho

class Game:
    INTERVALO = 20
    def __init__(self):
        self.__round = 1
        self.player1 = Player()
        self.player2 = Player()
        self.baralho = Baralho()
        self.__cartasDaVez = []
        self.__empate = 0
    
    @property
    def empate(self):
        return self.__empate

    @empate.setter
    def empate(self, value):
        self.__empate = value
    
    def round(self):
        self.__round += 1
        self.battle()

    def battle(self):
        carta1 = self.player1.mao.desempilha()
        carta2 = self.player2.mao.desempilha()
        print(f'\nCarta do Jogador 1: {carta1}\n\nCarta do Jogador 2: {carta2}\n')
        self.__cartasDaVez.append(carta1)
        self.__cartasDaVez.append(carta2)

        if carta1.numero == carta2.numero:
            saida = ''
            for carta in self.__cartasDaVez:
                saida += carta.__str__() + ' '
            print(f'\n***Empate!!***\n*** Cartas retidas: {saida}***')
            self.empate += 1
            print("\nIniciando rodada de desempate...\n")
            self.battle()
        elif carta1.numero < carta2.numero:
            self.coletaCartas(self.player2, self.__cartasDaVez)
            self.winner(self.player2)
        else:
            self.coletaCartas(self.player1, self.__cartasDaVez)
            self.winner(self.player1)


    def coletaCartas(self, player, lista):
        saida = ''
        for carta in lista:
            saida += carta.__str__() + ' '
        print(f"Cartas adquiridas: {saida}")
        for i in range(len(lista)):
            player.mao.insereFundo(lista.pop())
    
    def divideBaralho(self):
        i = 0
        while self.baralho.temCarta():
            if i%2 == 0:
                self.player1.mao.empilha(self.baralho.retirarCarta())
            else:
                self.player2.mao.empilha(self.baralho.retirarCarta())
            i += 1
    
    def winner(self, player):
        self.empate = 0
        player.win += 1
        print(f"""
                Jogador {player.id}: {player.name} venceu a rodada!
                Vitórias: {player.win}
                Total de Cartas:  {player.mao.tamanho()}\n   
                """)

    def mostraResultado(self):
        print(f"""
        #########################################

        {self.player1} -> Ganhou {self.player1.win} rodadas.
        Encerrou com {self.player1.mao.tamanho()} cartas na mão.

        ****************************************

        {self.player2} -> Ganhou {self.player2.win} rodadas.
        Encerrou com {self.player2.mao.tamanho()} cartas na mão.

        #########################################
        """)
    
    def start(self):
        name1 = input(f'Insira o nome do Jogador 1: ')
        self.player1.name = name1
        name2 = input(f'Insira o nome do Jogador 2: ')
        self.player2.name = name2
        self.divideBaralho()
        while True:
            if (self.__round % Game.INTERVALO) == 0:
                if input('\nDeseja [E]ncerrar o jogo agora ou [C]ontinuar até algum jogador não ter mais cartas?').upper() == 'E':
                    print("""
                    ###########################\n\n
                    Encerrando...\n\n
                    ###########################
                    """)
                    self.mostraResultado()
                    if input("Deseja [R]einiciar ou [E]ncerrar o jogo?").upper() == 'R':
                        self.restart()
                    break                
            print(f'\n\nRodada {self.__round}\n\n')
            self.round()
            input('Continuar...')

    def restart(self):
        self.player1 = Player()
        self.player2 = Player()
        self.baralho = Baralho()
        self.start()