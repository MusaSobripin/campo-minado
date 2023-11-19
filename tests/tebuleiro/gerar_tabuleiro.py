import random

def gerar_tabuleiro_dificil():
    # Dimensões do tabuleiro
    linhas, colunas = 24, 24
    # Número total de bombas
    num_bombas = 100

    # Inicializa o tabuleiro com células vazias (0)
    tabuleiro = [[0] * colunas for _ in range(linhas)]

    # Coloca as bombas no tabuleiro
    bombas_colocadas = 0
    while bombas_colocadas < num_bombas:
        x, y = random.randint(0, linhas - 1), random.randint(0, colunas - 1)
        if tabuleiro[x][y] != -1:
            tabuleiro[x][y] = -1
            bombas_colocadas += 1

    return tabuleiro

# Gerar o tabuleiro
tabuleiro_dificil = gerar_tabuleiro_dificil()

# Imprimir a matriz do tabuleiro
for linha in tabuleiro_dificil:
    print(' '.join(map(str, linha)))
