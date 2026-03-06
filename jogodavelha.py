tabuleiro = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
jogador_da_vez = "X"
def mostar_tabuleiro():
    print(f"{tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}")
    print("---------")
    print(f"{tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}")
    print("---------")
    print(f"{tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}")

def verificar_vitoria(tabuleiro, combinacoes_de_vitoria,jogador_da_vez):
    for combinacao in combinacoes_de_vitoria:
        if (tabuleiro[combinacao[0]] == jogador_da_vez and
            tabuleiro[combinacao[1]] == jogador_da_vez and
            tabuleiro[combinacao[2]] == jogador_da_vez):
            return True
    return False
combinacoes_de_vitoria = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [0,3,6],
    [1,4,7],
    [2,5,8],
    [0,4,8],
    [2,4,6]
]
jogadas = 0 
while True:
    mostar_tabuleiro()
    posicao = int(input("Escolha uma posiçao 0 a 8:"))
    if posicao < 0 or posicao > 8:
        print("Posiçao negada")
        continue
    if tabuleiro[posicao] != " ":
        print("casa ocupada")
        continue
    tabuleiro[posicao] = jogador_da_vez
    jogadas += 1 #aumenta só quando a jogada é válida
    if verificar_vitoria(tabuleiro,combinacoes_de_vitoria,jogador_da_vez):
        print(f"{jogador_da_vez} Venceu!")
        break

    if jogadas == 9:
        print("deu empate")
        break
    
    if jogador_da_vez == "X":
        jogador_da_vez = "O"
    else:
        jogador_da_vez = "X"


