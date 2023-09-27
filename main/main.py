import tkinter as tk
import random

# Função para criar um tabuleiro de jogo vazio
def criar_tabuleiro(linhas, colunas):
    return [[0] * colunas for _ in range(linhas)]

# Função para adicionar bombas aleatoriamente ao tabuleiro
def adicionar_bombas(tabuleiro, num_bombas):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    bombas_adicionadas = 0

    while bombas_adicionadas < num_bombas:
        x = random.randint(0, linhas - 1)
        y = random.randint(0, colunas - 1)

        if tabuleiro[x][y] != -1:
            tabuleiro[x][y] = -1
            bombas_adicionadas += 1

# Função para calcular o número de bombas adjacentes a uma célula
def calcular_vizinhos(tabuleiro, x, y):
    linhas, colunas = len(tabuleiro), len(tabuleiro[0])
    bomb_count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            if 0 <= x + i < linhas and 0 <= y + j < colunas:
                if tabuleiro[x + i][y + j] == -1:
                    bomb_count += 1

    return bomb_count

# Função para revelar uma célula
def revelar_celula(x, y):
    if tabuleiro[x][y] == -1:
        game_over()
    else:
        vizinhos = calcular_vizinhos(tabuleiro, x, y)
        tabuleiro[x][y] = vizinhos
        buttons[x][y]['text'] = str(vizinhos)
        buttons[x][y]['state'] = 'disabled'
        if vizinhos == 0:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if 0 <= x + i < linhas and 0 <= y + j < colunas and buttons[x + i][y + j]['state'] == 'normal':
                        revelar_celula(x + i, y + j)

# Função para mostrar o resultado do jogo
def game_over():
    for x in range(linhas):
        for y in range(colunas):
            if tabuleiro[x][y] == -1:
                buttons[x][y]['text'] = 'X'
            buttons[x][y]['state'] = 'disabled'
    status_label.config(text='Game Over!')

# Função para iniciar um novo jogo
def novo_jogo():
    global tabuleiro
    tabuleiro = criar_tabuleiro(linhas, colunas)
    adicionar_bombas(tabuleiro, num_bombas)
    status_label.config(text='')
    
    for x in range(linhas):
        for y in range(colunas):
            buttons[x][y]['text'] = ''
            buttons[x][y]['state'] = 'normal'

# Configurações do jogo
linhas, colunas = 8, 8
num_bombas = 10

# Inicialização do tabuleiro
tabuleiro = criar_tabuleiro(linhas, colunas)
adicionar_bombas(tabuleiro, num_bombas)

# Configuração da interface gráfica
window = tk.Tk()
window.title('Campo Minado')
buttons = [[None] * colunas for _ in range(linhas)]

for x in range(linhas):
    for y in range(colunas):
        buttons[x][y] = tk.Button(window, width=3, height=1, command=lambda x=x, y=y: revelar_celula(x, y))
        buttons[x][y].grid(row=x, column=y)

status_label = tk.Label(window, text='', padx=10)
status_label.grid(row=linhas, columnspan=colunas)

novo_jogo_button = tk.Button(window, text='Novo Jogo', command=novo_jogo)
novo_jogo_button.grid(row=linhas + 1, columnspan=colunas)

window.mainloop()
