'''


***** [0.32 pontos]: Checando partida unica (n = 5, m = 3, jogadas = (1,)) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.32 pontos]: Checando partida unica (n = 5, m = 3, jogadas = (2,)) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.32 pontos]: Checando partida unica (n = 9, m = 2, jogadas = (1, 2, 2)) - Falhou *****
AssertionError: Deveria comecar com o oponente

***** [0.32 pontos]: Checando partida unica (n = 9, m = 2, jogadas = (1, 2, 1)) - Falhou *****
AssertionError: Deveria comecar com o oponente

***** [0.32 pontos]: Checando partida unica (n = 11, m = 3, jogadas = (2, 3)) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.01 pontos]: Checando partida unica que o computador ganha na primeira jogada (n = 25, m = 25, jogadas = ()) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.01 pontos]: Checando partida unica que o computador ganha na primeira jogada (n = 2, m = 2, jogadas = ()) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.01 pontos]: Checando partida unica que o computador ganha na primeira jogada (n = 1, m = 1, jogadas = ()) - Falhou *****
AssertionError: Computador deveria ter ganhado

***** [0.12 pontos]: Checando campeonato (partida 1: n = 5, m = 3, jogadas = [1]; partida 2: n = 5, m = 3, jogadas = [2]; partida 3: n = 9, m = 2, jogadas = [1, 2, 2]) - Falhou *****
AssertionError: Computador deveria ter ganhado


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
    global fim_de_jogo
    fim_de_jogo = False
    vez_computador = False
    
    if n <= m:
         print("O computador tirou ",n," peças.")
         print("Fim do jogo! O computador ganhou!")
         fim_de_jogo = True
    else: 
        if n % (m + 1) == 0 or n == m:
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
    '''
    ***** [0.15 pontos]: Testando usuario_escolhe_jogada (n = 5, m = 3, resposta 2) - Falhou *****
    Timeout

    ***** [0.15 pontos]: Testando usuario_escolhe_jogada (n = 6, m = 4, resposta 1) - Falhou *****
    Timeout

    ***** [0.15 pontos]: Testando usuario_escolhe_jogada (n = 5, m = 3, resposta 3) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada quando n <= m (n = 3, m = 5, resposta 2) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada quando n <= m (n = 3, m = 5, resposta 3) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada quando n <= m (n = 1, m = 1, resposta 1) - Falhou *****
    Timeout

    ***** [0.04 pontos]: Testando usuario_escolhe_jogada com jogada inválida: valor > m (n = 5, m = 3, respostas 5, 2) - Falhou *****
    Timeout

    ***** [0.04 pontos]: Testando usuario_escolhe_jogada com jogada inválida: valor > m (n = 5, m = 3, respostas 4, 3) - Falhou *****
    Timeout

    ***** [0.04 pontos]: Testando usuario_escolhe_jogada com jogada inválida: valor <= 0 (n = 5, m = 3, respostas 0, 2) - Falhou *****
    Timeout

    ***** [0.04 pontos]: Testando usuario_escolhe_jogada com jogada inválida: valor <= 0 (n = 5, m = 3, respostas -1, 3) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada com jogada inválida se n <= m (n = 3, m = 5, respostas 4, 3) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada com jogada inválida se n <= m (n = 3, m = 5, respostas 4, 1) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada com jogada inválida se n <= m (n = 3, m = 3, respostas 4, 3) - Falhou *****
    Timeout

    ***** [0.01 pontos]: Testando usuario_escolhe_jogada com jogada inválida se n <= m (n = 3, m = 3, respostas 4, 1) - Falhou *****
    Timeout

    ***** [0.05 pontos]: Testando usuario_escolhe_jogada com múltiplas jogadas inválidas (n = 5, m = 3, respostas 5, 0, -1, 2) - Falhou *****
    Timeout
    '''
    
            
    jogada = input("Quantas peças você vai tirar? ")
    jogada = int(jogada)
    # Valida jogada
    if jogada > m or jogada < 1:
            while jogada > m or jogada < 1:
                jogada = input("Oops! Jogada inválida! Tente de novo ")
                jogada = int(jogada)
    # Se jogada é válida, analisa todos os cenários se n é menor ou igual a m e retorna
    if n <= m:
        if jogada < n:
            return jogada
        else:
            return n
    # # Se jogada é válida, analisa todos os cenários se n maior que m e retorna
    else: 
        if n < 1:
            return 0
        elif n >= m:
            return n
        else:
            return jogada
    

print(usuario_escolhe_jogada(3,5))


# partida()




# def campeonato():
    # Essa nova função deve realizar três partidas seguidas do jogo e, ao final, mostrar o placar dessas três partidas e indicar o vencedor do campeonato. 
    # O placar deve ser impresso na forma
    # Placar: Você ??? X ??? Computador
    # Dado que é possível jogar partidas individuais ou campeonatos, seu programa deve começar solicitando ao usuário que escolha se prefere jogar:
    # apenas uma partida (opção 1) ou um campeonato (opção 2)
    