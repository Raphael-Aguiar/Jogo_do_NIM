# Jogo do NIM

def campeonato():
    modo = input("Bem-vindo ao jogo do NIM! Escolha: /n 1 - para jogar uma partida isolada; /n 2 - para jogar um campeonato: ")
    
    if modo == "1":
        print("Voce escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato! /n **** Rodada 1 ****")
        partida()
        print("**** Rodada 2 ****")
        partida()
        print("**** Rodada 3 ****")
        partida()
    print("**** Final do campeonato! /n Placar: Você 0 X 3 Computador ****")


def partida():
    n = input("Quantas peças? ")
    m = input("Limite de peças por jogada? ")
    n = int(n)
    m = int(m)
    fim_de_jogo = False
    vez_computador = False
    
    if n <= m:
        print("Computador começa!")
        print("O computador tirou",n," peças.")
        print("Fim do jogo! O computador ganhou!")
        fim_de_jogo = True

    else: 
        if n % (m + 1) == 0:
            print("Computador começa!")
            vez_computador = True
        else:
            print("Voce começa!")
            vez_computador = False
    
    if fim_de_jogo != True:
        
        while n > 0 and fim_de_jogo == False:
    
            if vez_computador == True:
                lance_computador = computador_escolhe_jogada(n,m)
                n = n - lance_computador
                print("O computador tirou ",lance_computador," peças.")
    
                if n <= 0:
                    print("Fim do jogo! O computador ganhou!")
                    fim_de_jogo = True
    
                else:
                    print("agora restam",n," peças no tabuleiro.")
                    vez_computador = False
    
            else:
                lance_usuario = usuario_escolhe_jogada(n,m)
                n = n - lance_usuario
                print("Você tirou",lance_usuario," peças.")

                if n <= 0:
                    print("Fim do jogo! você ganhou!")
                    fim_de_jogo = True

                else:
                    print("agora restam ",n," peças no tabuleiro.")
                    vez_computador = True

def computador_escolhe_jogada(n,m):
    if n > m:
        jogada = 1
        
        while (n - jogada) % (m + 1) != 0:
            jogada = jogada + 1
        
        if jogada < m:
            return jogada
        
        else:
            return m
    
    else:
        return n   

def usuario_escolhe_jogada(n,m):
    # recebe os mesmos parâmetros, solicita que o jogador informe sua jogada e verifica se o valor informado é válido.
    # Se o valor informado for válido, a função deve devolvê-lo; caso contrário, deve solicitar novamente ao usuário que informe uma jogada válida.
    def valida_jogada(j,n,m):
      if j > m or j > n or j < 1:
        return False
      else:
        return True

    jogada = input("Quantas peças você vai tirar? ")
    jogada = int(jogada)
    validade = False
    validade = valida_jogada(jogada,n,m)
    while validade == False:
            jogada = input("Oops! Jogada inválida! Tente de novo ")
            jogada = int(jogada)
            validade = valida_jogada(jogada,n,m)   
    return jogada

partida()
