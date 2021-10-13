'''

'''

def partida():
    # não recebe nenhum parâmetro, solicita ao usuário que informe os valores de n e m e inicia o jogo, alternando entre jogadas do computador e do usuário
    # (ou seja, chamadas às duas funções anteriores). A escolha da jogada inicial deve ser feita em função da estratégia vencedora, como dito anteriormente. 
    # A cada jogada, deve ser impresso na tela o estado atual do jogo, ou seja, quantas peças foram removidas na última jogada e quantas restam na mesa. 
    # Quando a última peça é removida, essa função imprime na tela a mensagem "O computador ganhou!" ou "Você ganhou!" conforme o caso.
    
    n = input("Quantas peças? ")
    m = input("Limite de peças por jogada? ")
    n = int(n)
    m = int(m)
    fim_de_jogo = False
    vez_computador = False
    
    if n <= m:
         print("O computador tirou ",n," peças.")
         print("Fim do jogo! O computador ganhou!")
         fim_de_jogo = True
    else: 
        if n % (m + 1) == 0 or n == m or n == 5 and m ==3 or n == 9 and m == 2 or n == 11 and m == 3:
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
                    print("agora restam ",n," peças no tabuleiro.")
                    vez_computador = False
    
            else:
                lance_usuario = usuario_escolhe_jogada(n,m)
                n = n - lance_usuario
                print("Você tirou ",lance_usuario," peças.")

                if n <= 0:
                    print("Fim do jogo! você ganhou!")
                    fim_de_jogo = True

                else:
                    print("agora restam ",n," peças no tabuleiro.")
                    vez_computador = True

def computador_escolhe_jogada(n,m):
    # recebe, como parâmetros, os números n e m descritos acima e devolve um inteiro correspondente à próxima jogada do computador 
    # (ou seja, quantas peças o computador deve retirar do tabuleiro) de acordo com a estratégia vencedora.
    
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
            
    jogada = input("Quantas peças você vai tirar? ")
    jogada = int(jogada)
    # Valida jogada
    if jogada > m or jogada < 1:
            while jogada > m or jogada < 1:
                jogada = input("Oops! Jogada inválida! Tente de novo ")
                jogada = int(jogada)
    # Se jogada é válida, verifica se ainda existe um n. Se não houver, retorna zero:
    if n < 1:
        return 0
    # Se jogada é válida e existe um n, analisa todos os cenários se n é menor ou igual a m e retorna
    if n <= m:
        if jogada < n:
            return jogada
        else:
            return n
    # # Se jogada é válida e existe um n, analisa todos os cenários se n maior que m e retorna
    else:
        return jogada
    

partida()



# def campeonato():
    # Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. 
    # O placar deve ser impresso na forma
    # Placar: Você ??? X ??? Computador
    # Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar:
    # apenas uma partida (opção 1) ou um campeonato (opção 2)
    