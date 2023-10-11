import tkinter as tk
import tkinter.messagebox
import random
import time

class CampoMinado:
    def __init__(self, root):
        self.root = root
        self.root.title("Campo Minado")
        
        self.niveis = {
            "Fácil": (8, 8, 10),
            "Intermediário": (10, 16, 30),
            "Difícil": (24, 24, 100)
        }
        
        self.nivel = None
        self.linhas = 0
        self.colunas = 0
        self.bombas = 0
        self.tabuleiro = None
        self.botoes = []
        self.jogo_encerrado = False
        self.bombas_posicoes = set()  # Rastrear as posições das bombas
        
        self.tempo_inicial = None
        self.tempo_passado = 0
        self.timer = None
        
        self.placar_label = tk.Label(root, text="Tempo: 0 segundos  Bombas restantes: 0")
        self.placar_label.pack()
        
        self.tabuleiro_frame = None
        
        self.criar_tabuleiro()
        self.criar_menu_niveis()
    
    def criar_menu_niveis(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=10)
        
        tk.Label(menu_frame, text="Escolha um nível:").pack()
        
        for nivel, (linhas, colunas, bombas) in self.niveis.items():
            tk.Button(menu_frame, text=nivel, command=lambda l=linhas, c=colunas, b=bombas: self.iniciar_jogo(l, c, b)).pack()
    
    def iniciar_jogo(self, linhas, colunas, bombas):
        self.nivel = (linhas, colunas, bombas)
        self.linhas = linhas
        self.colunas = colunas
        self.bombas_posicoes = set()
        self.bombas = bombas
        self.jogo_encerrado = False
        self.tempo_inicial = None
        self.tempo_passado = 0
        self.bombas_posicoes = set()  # Limpar as posições das bombas antigas
        
        # Verificar se há um tabuleiro anterior e destruí-lo
        if self.tabuleiro_frame:
            self.tabuleiro_frame.destroy()
        
        self.criar_tabuleiro()
        self.plantar_bombas()
        self.atualizar_placar()
    
    def criar_tabuleiro(self):
        self.tabuleiro_frame = tk.Frame(self.root)
        self.tabuleiro_frame.pack()
        
        self.tabuleiro = [[0 for _ in range(self.colunas)] for _ in range(self.linhas)]
        self.botoes = [[None for _ in range(self.colunas)] for _ in range(self.linhas)]
        
        for i in range(self.linhas):
            for j in range(self.colunas):
                btn = tk.Button(self.tabuleiro_frame, width=2, height=1)
                btn.grid(row=i, column=j)
                btn.bind("<Button-1>", lambda event, i=i, j=j: self.clicar(i, j))
                btn.bind("<Button-3>", lambda event, i=i, j=j: self.marcar_bandeira(i, j))
                self.botoes[i][j] = btn
    
    def plantar_bombas(self):
        bombas_plantadas = 0
        while bombas_plantadas < self.bombas:
            i, j = random.randint(0, self.linhas - 1), random.randint(0, self.colunas - 1)
            if self.tabuleiro[i][j] != -1:
                self.tabuleiro[i][j] = -1
                bombas_plantadas += 1
                self.bombas_posicoes.add((i, j))  # Adicionar a posição da bomba
        
        for i, j in self.bombas_posicoes:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= i + dr < self.linhas and 0 <= j + dc < self.colunas and self.tabuleiro[i + dr][j + dc] != -1:
                        self.tabuleiro[i + dr][j + dc] += 1
    
    def clicar(self, row, col):
        if self.jogo_encerrado or self.tabuleiro[row][col] == -2:
            return
        
        if self.tempo_inicial is None:
            self.tempo_inicial = time.time()
        
        if self.tabuleiro[row][col] == -1:
            self.mostrar_bombas()
            self.mostrar_mensagem("Você perdeu!")
            self.jogo_encerrado = True
            self.finalizar_partida()
        else:
            self.revelar_celula(row, col)
            self.verificar_vitoria()
    
    def mostrar_mensagem(self, mensagem):
        resposta = tkinter.messagebox.askquestion("Resultado", mensagem + f"\nTempo: {self.tempo_passado} segundos\nDeseja jogar novamente?")
        if resposta == "yes":
            self.iniciar_jogo(*self.nivel)
        else:
            self.root.quit()
    
    def mostrar_bombas(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] == -1:
                    self.botoes[i][j].config(text="💣", state="disabled")


    
    def calcular_vizinhos(self, x, y):
        linhas, colunas = self.linhas, self.colunas
        bomb_count = 0 
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < linhas and 0 <= y + j < colunas:
                    if self.tabuleiro[x + i][y + j] == -1:
                        bomb_count += 1

        return bomb_count

    
    """def revelar_celula(self, row, col):
        if self.tabuleiro[row][col] != 0:
            self.botoes[row][col].config(text=str(self.tabuleiro[row][col]), state="disabled")
        else:
            self.botoes[row][col].config(state="disabled")
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= row + dr < self.linhas and 0 <= col + dc < self.colunas and self.tabuleiro[row + dr][col + dc] != -1 and self.tabuleiro[row + dr][col + dc] != -2:
                        self.revelar_celula(row + dr, col + dc)
        self.tabuleiro[row][col] = -2"""

    def revelar_celula(self, x, y):
        if self.tabuleiro[x][y] == -1:
            self.finalizar_partida()
        else:
            vizinhos = self.calcular_vizinhos(self.tabuleiro, x, y)
            self.tabuleiro[x][y] = vizinhos
            self.botoes[x][y]['text'] = str(vizinhos)
            self.botoes[x][y]['state'] = 'disabled'
            if vizinhos == 0:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if 0 <= x + i < self.linhas and 0 <= y + j < self.colunas and self.botoes[x + i][y + j]['state'] == 'normal':
                            self.revelar_celula(x + i, y + j)

    def marcar_bandeira(self, row, col):
        if self.jogo_encerrado:
            return
        
        if self.tabuleiro[row][col] != -2:
            if self.tabuleiro[row][col] == -1:
                self.botoes[row][col].config(text="😥", state="disabled")
            else:
                self.botoes[row][col].config(text="😥")
            self.tabuleiro[row][col] = -2
        else:
            self.botoes[row][col].config(text="", state="normal")
            self.tabuleiro[row][col] = self.contar_vizinhos(row, col)
    
    def contar_vizinhos(self, row, col):
        vizinhos = 0
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if 0 <= row + dr < self.linhas and 0 <= col + dc < self.colunas and self.tabuleiro[row + dr][col + dc] == -2:
                    vizinhos += 1
        return vizinhos
    
    def atualizar_placar(self):
        if self.tempo_inicial is not None and not self.jogo_encerrado:
            tempo_atual = int(time.time() - self.tempo_inicial)
        else:
            tempo_atual = self.tempo_passado
        
        bombas_restantes = self.bombas - sum(1 for i, j in self.bombas_posicoes if self.tabuleiro[i][j] == -2)
        self.placar_label.config(text=f"Tempo: {tempo_atual} segundos  Bombas restantes: {bombas_restantes}")
        if not self.jogo_encerrado:
            self.root.after(1000, self.atualizar_placar)
    
    def finalizar_partida(self):
        self.tempo_passado = int(time.time() - self.tempo_inicial)
        self.atualizar_placar()
        self.mostrar_bombas()
    
    def verificar_vitoria(self):
        celulas_livres = sum(row.count(0) for row in self.tabuleiro)
        celulas_abertas = sum(row.count(-2) for row in self.tabuleiro)
        if celulas_abertas == celulas_livres:
            self.mostrar_bombas()
            self.mostrar_mensagem(f"Você ganhou em {self.tempo_passado} segundos!")
            self.jogo_encerrado = True
            self.finalizar_partida()
    
    def reiniciar_jogo(self):
        self.jogo_encerrado = False
        self.iniciar_jogo(*self.nivel)

if __name__ == "__main__":
    root = tk.Tk()
    game = CampoMinado(root)
    root.mainloop()