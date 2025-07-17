from auxiliar import monstrar_mapa, criar_mapa, criar_enbarcacao, jogada, mudar_mapa, mudar_mapa2,nome_jogador

#Trabalho Final - Batalha Naval
#Arquivo de Funções auxiliares
#
#Grupo composto por: 
#   Renan Alves de Souza do Nascimento
#   Lucas de Araujo Contreiras
#   Ygo Rodrigo Fernandes de Souza
#
print("Bem vindo ao Batalha Naval.")
regras = input("Digite R para ver as regras do jogo ou então aperte qualquer outra tecla para começar: ")
if regras == "R":
    print("Batalha naval é um jogo de tabuleiro de dois jogadores, no qual os jogadores têm de adivinhar em que quadrados estão os navios do oponente;\n\n"
    "* O jogador1 começa atacando alguma cordenada dada por uma letra entre A a J e logo em seguida um numero de 0 a 9;\n"
    "* Se qualquer jogador acertar, não passará a rodada para o próximo, com isso, o jogador poderá jogar novamente;\n"
    "* O jogo acaba quando o primeiro jogador afundar todas as embarcações do adversário;\n" 
    "* Use o comando: 'sair' se deseja sair da partida;\n"
    "* Use o comando: reiniciar se deseja 'reiniciar' a partida;\n"
    "* Use o comando embarcacoes se deseja ver quantas embarcações foram afundadas.\n\n")
# as siglas asseguir são os nomes das embarcações
# pt = porta aviões
# sub = submarino
# tq = navios tanque
# ctt = contratorpedeiros
# as variações numericas são do jogador 1 e as variações do Alfabeto são do jogador 2
# (っ◕‿◕)っ
# (っ＾▿＾)
# ( ˘︹˘ )
# (ง︡'-'︠)ง
# (¬‿¬)
# (͠≖ ͜ʖ͠≖)

def main():
    '''Função Principal do jogo onde ira coordenar todas as funções'''
    jogador1,jogador2 = nome_jogador()
    mapa = criar_mapa(10)
    mapa2 = criar_mapa(10)
    monstrar_mapa(mapa, mapa2)
    pt = criar_enbarcacao(5, mapa)
    pt_A = criar_enbarcacao(5, mapa)
    tq, tq2 = criar_enbarcacao(4, mapa), criar_enbarcacao(4, mapa)
    tq_A,tq_B = criar_enbarcacao(4, mapa),criar_enbarcacao(4, mapa)
    ctt,ctt2,ctt3 = criar_enbarcacao(3, mapa), criar_enbarcacao(3, mapa), criar_enbarcacao(3, mapa)
    ctt_A, ctt_B, ctt_C = criar_enbarcacao(3, mapa),criar_enbarcacao(3, mapa),criar_enbarcacao(3, mapa)
    sub,sub2,sub3,sub4 = criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa)
    sub_A,sub_B,sub_C,sub_D = criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa),criar_enbarcacao(2, mapa)
    fragata = [pt, tq, tq2, ctt, ctt2, ctt3, sub, sub2, sub3, sub4]
    fragata2 = [pt_A, tq_A, tq_B, ctt_A, ctt_B, ctt_C, sub_A, sub_B, sub_C, sub_D]
    tentativas = []
    tentativas2 = []
    num_embarcacao = 10
    num_embarcacao2 = 10 

    while num_embarcacao != 0 or num_embarcacao2 != 0:   
        x1 = 0
        x2 = 0
        acertou = True
        while acertou == True:
            
            mapa = mudar_mapa(jogada(), mapa, fragata, tentativas)
            print("Vez do "+jogador1+" jogar")
            acertou = mapa[1]
            mapa = mapa[0]
            monstrar_mapa(mapa, mapa2)
            print('Quantidade de Embarcações do {}: {}\n'.format(jogador1,num_embarcacao2))
            print('Quantidade de Embarcações do {}: {}\n'.format(jogador2,num_embarcacao))
            for i in mapa:
                for j in i:
                    if j == "X":
                        x1 += 1  
            if acertou == False:
                acertou2 = True
                print("Vez do "+jogador2+" jogar")

        while acertou2 == True:
            
            mapa2 = mudar_mapa2(jogada(), mapa2, fragata2, tentativas2)
            print("Vez do "+jogador2+" jogar")
            acertou = mapa2[1]
            mapa2 = mapa2[0]
            monstrar_mapa(mapa, mapa2)
            print('Quantidade de Embarcações do {}: {}\n'.format(jogador1,num_embarcacao2))
            print('Quantidade de Embarcações do {}: {}\n'.format(jogador2,num_embarcacao))
            for i in mapa:
                for j in i:
                    if j == "X":
                        x2 += 1
            if acertou2 == False:
                acertou = True
                print("Vez do "+jogador1+" jogar")
        
        if x1 == 30:
            print("Parabéns "+ jogador1 +" é o vencedor")
            fragata = []
        elif x2 == 30:
            print("Parabéns "+ jogador2 +" é o vencedor")
            fragata2 = []

    return jogada()

if __name__ == "__main__":
    main()
