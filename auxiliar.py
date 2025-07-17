import random
#Trabalho Final - Batalha Naval
#Arquivo de Funções auxiliares
#
#Grupo composto por: 
#   Renan Alves de Souza do Nascimento
#   Lucas de Araujo Contreiras
#   Ygo Rodrigo Fernandes de Souza
#

global jogador1
global jogador2

def nome_jogador():
    '''funcao que define o nome dos jogadores'''
    global jogador1
    global jogador2
    jogador1= input("Qual o nome do 1° jogador : ")
    jogador2= input("Qual o nome do 2° jogador : ")
    return jogador1,jogador2

def criar_mapa(tamanho):
    '''funcao que recebe um parametro de entrada e retorna 
    a criacao das aguas'''
    return [["~" for i in range(tamanho)] for i in range(tamanho)]

def monstrar_mapa(mapa, mapa2):
    '''funcao que mostra o mapa dos jodaores na tela'''
    abecedario = "ABCDEFGHIJ"
    print("                 Mapa do ",jogador1)
    for i in range(len(mapa2)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()

    for fila in range(len(mapa2)):
        print(f"{fila} {mapa2[fila]}")
    print("-"*52)
    abecedario = "ABCDEFGHIJ"
    print("                     Mapa do ",jogador2)
    for i in range(len(mapa)):
        letra = abecedario[i]
        print(f"   {(letra)}", end=" ")
    print()
    for fila in range(len(mapa)):
        print(f"{fila} {mapa[fila]}")


def jogada():
    '''funcao que define as coordenads e alguns comandos, como sair e reiniciar'''
    print("Jogue no seguinte formato com letra Maiúculas ou Minusculas: A,1\nDigite 'sair' para sair do jogo\nDigite 'reiniciar' para reiniciar o jogo\n")
    coordenadas = input("Coordenadas: ")
    if coordenadas == "sair":
        exit()
    if coordenadas == "reiniciar":
        jogada()
    posicao = coordenadas.split(",")

    coluna = str.upper(posicao[0])
    if coluna == "A":
        coluna = 0
    elif coluna == "B":
        coluna = 1
    elif coluna == "C":
        coluna = 2
    elif coluna == "D":
        coluna = 3
    elif coluna == "E":
        coluna = 4
    elif coluna == "F":
        coluna = 5
    elif coluna == "G":
        coluna = 6
    elif coluna == "H":
        coluna = 7
    elif coluna == "I":
        coluna = 8
    elif coluna == "J":
        coluna = 9
    linha = int(posicao[1])
    return(linha,coluna)

def mudar_mapa(chute, mapa, fragata, tentativas):
    '''funcao que recebe quatro parametros e cria uma interacao entre os jogadores
    com base nos erros e acertos'''
    acertou = False
    if chute in tentativas:
        print(jogador2+': Ha Ha acertou a água!!! (っ＾▿＾)\n')
        print(jogador1+": Eu ainda não terminei (͠≖ ͜ʖ͠≖)\n")
        acertou = False
        return mapa, acertou
    list.append(tentativas, chute)
    for i in fragata:
        if chute in i:
            print(jogador1+": Agora peguei você (¬‿¬) \n")
            print(jogador2+": Isso Não vai acabar assim (ง︡'-'︠)ง\n")
            mapa[chute[0]][chute[1]] = 'X'
            acertou = True
            return mapa, acertou
    mapa[chute[0]][chute[1]] = "*"
    
    return mapa,acertou

def mudar_mapa2(chute2, mapa2, fragata2, tentativas2):
    '''funcao que recebe de parametros de entrada, tamanho e mapa
    para gerar aleatoriamente as embarcações'''
    acertou2 = False
    if chute2 in tentativas2:
        print(jogador1+': Ha Ha acertou a água!!! (っ＾▿＾)\n')
        print(jogador2+": Eu ainda não terminei (͠≖ ͜ʖ͠≖)\n")
        acertou2 = False
        return mapa2, acertou2
    list.append(tentativas2, chute2)
    for i in fragata2:
        if chute2 in i:
            print(jogador2+": Agora peguei você (¬‿¬)\n")
            print(jogador1+": Isso Não vai acabar assim (ง︡'-'︠)ง\n")
            mapa2[chute2[0]][chute2[1]] = 'X'
            acertou2 = True
            return mapa2, acertou2
    mapa2[chute2[0]][chute2[1]] = "*"
    return mapa2,acertou2

def criar_enbarcacao(tamanho, mapa):
    '''funcao que recebe quatro parametros e cria uma interacao entre os jogadores
    com base nos erros e acertos'''
    sentido = random.randint(0, 1)
    if sentido == 0:
        lin_barco = [random.randint(0, len(mapa) - 1)] * tamanho
        col = random.randint(0, len(mapa) - tamanho)
        col_barco = list(range(col, col + tamanho))
        coordenadas = list(zip(lin_barco, col_barco))
    else:
        col_barco = [random.randint(0, len(mapa) - 1)] * tamanho
        lin = random.randint(0, len(mapa) - tamanho)
        lin_barco = list(range(lin, lin + tamanho))
        coordenadas = list(zip(lin_barco, col_barco))
    return list(coordenadas)





