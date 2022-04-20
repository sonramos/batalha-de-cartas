from PilhaEncadeada import PilhaException
from Player import Player
from Baralho import Baralho

class Game:
    INTERVALO = 5
    def __init__(self):
        self.__round = 0
        self.player1 = Player()
        self.player2 = Player()
        self.baralho = Baralho()
        self.__cartasDaVez = []
    
    def round(self):
        self.__round += 1
        self.battle()

    def battle(self):
        try:
            carta1 = self.player1.desempilhaCarta()
        except:
            raise PilhaException(f"{self.player1} nao possui mais cartas na mao.",self.game_winner(self.player2))
        try:
            carta2 = self.player2.desempilhaCarta()
        except:
            raise PilhaException(f"{self.player2} nao possui mais cartas na mao.",self.game_winner(self.player1))
        print(f'\n***** Carta - Jogador 1: {carta1} *****\n\n***** Carta - Jogador 2: {carta2} *****\n\n')
        self.__cartasDaVez.append(carta1)
        self.__cartasDaVez.append(carta2)

        if carta1.numero == carta2.numero:
            saida = ''
            for carta in self.__cartasDaVez:
                saida += carta.__str__() + ' '
            print(f'\n***Empate!!***\n*** Cartas retidas: {saida}***')
            print("\nIniciando rodada de desempate...\n")
            self.battle()
        elif carta1.numero < carta2.numero:
            print(f"{self.player2} venceu a rodada!")
            self.player2.win += 1
            self.coletaCartas(self.player2, self.__cartasDaVez)
            self.close_round()            
        else:
            print(f"{self.player1} venceu a rodada!")
            self.player1.win += 1
            self.coletaCartas(self.player1, self.__cartasDaVez)
            self.close_round()

    def coletaCartas(self, player, lista):
        saida = ''
        for carta in lista:
            saida += carta.__str__() + ' '
        print(f"\n***** Cartas adquiridas: {saida} *****")
        #for i in range(len(lista)):
        while lista:
            player.recebeCartaFundo(lista.pop())
    
    def divideBaralho(self):
        i = 0
        while self.baralho.temCarta():
            if i%2 == 0:
                self.player1.empilhaCarta(self.baralho.retirarCarta())
            else:
                self.player2.empilhaCarta(self.baralho.retirarCarta())
            i += 1
    
    def close_round(self):
        print(f"""
        ###############################################
        #                                             #
                    Vitórias {self.player1}: {self.player1.win} 
                    Cartas na mão:  {self.player1.totalCartas()}          
        #                                             #
        ###############################################

        ###############################################
        #                                             #
                    Vitórias {self.player2}: {self.player2.win} 
                    Cartas na mão:  {self.player2.totalCartas()}
        #                                             #
        ###############################################
        """)

    def game_winner(self, player):
        print(f"""
        {player} venceu o jogo!
        Total de Vitórias: {player.win}
        Total de Cartas:  {player.totalCartas()}\n   
        """)
        exit()

    def mostraResultado(self):
        print(f"""
        #########################################

        {self.player1} -> Ganhou {self.player1.win} rodadas.
        Encerrou com {self.player1.totalCartas()} cartas na mão.

        ****************************************

        {self.player2} -> Ganhou {self.player2.win} rodadas.
        Encerrou com {self.player2.totalCartas()} cartas na mão.

        #########################################
        """)
    
    def start(self):
        name1 = input(f'Insira o nome do Jogador 1: ')
        self.player1.name = name1
        name2 = input(f'Insira o nome do Jogador 2: ')
        self.player2.name = name2
        self.divideBaralho()
        while True:
            print(f'\n\nRodada {self.__round+1}\n\n')
            self.round()
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
            input('Continuar...')

    def restart(self):
        self.player1 = Player()
        self.player2 = Player()
        self.baralho = Baralho()
        self.__round = 0 #tinha faltado fazer isso
        self.start()