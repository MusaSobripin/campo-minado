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
        self.bombas_posicoes = set()
        self.bandeiras = set()

        self.tempo_inicial = None
        self.tempo_passado = 0
        self.timer = None

        self.tabuleiro_frame = None

        self.criar_tabuleiro()
        self.criar_menu_niveis()

    def criar_menu_niveis(self):
        menu_frame = tk.Frame(self.root)
        menu_frame.pack(pady=10)

        label = tk.Label(menu_frame, text="Escolha um nível:")
        label.pack()

        self.niveis = [("Fácil", 8, 8, 10), ("Intermediário", 10, 16, 30), ("Difícil", 24, 24, 100)]
        buttons = []

        for nivel, linhas, colunas, bombas in self.niveis:
            button = tk.Button(menu_frame, text=nivel, command=lambda l=linhas, c=colunas, b=bombas: self.iniciar_jogo(l, c, b))
            button.pack()
            buttons.append(button)

        return label, buttons
    
    def iniciar_jogo(self, linhas, colunas, bombas):
        self.nivel = (linhas, colunas, bombas)
        self.linhas = linhas
        self.colunas = colunas
        self.bombas_posicoes = set()
        self.bombas = bombas
        self.jogo_encerrado = False
        self.tempo_inicial = None
        self.tempo_passado = 0
        self.bandeiras = set()

        if self.tabuleiro_frame:
            self.tabuleiro_frame.destroy()

        self.criar_tabuleiro()
        self.plantar_bombas()

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
                self.bombas_posicoes.add((i, j))

        for i, j in self.bombas_posicoes:
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if 0 <= i + dr < self.linhas and 0 <= j + dc < self.colunas and self.tabuleiro[i + dr][j + dc] != -1:
                        self.tabuleiro[i + dr][j + dc] += 1

    def clicar(self, row, col):
        if self.jogo_encerrado or (row, col) in self.bandeiras:
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
        resposta = tkinter.messagebox.askquestion("Resultado", mensagem + f"\nDeseja jogar novamente?")
        if resposta == "yes":
            self.iniciar_jogo(*self.nivel)
        else:
            self.root.quit()
            raise SystemExit  # Lançar uma exceção SystemExit quando o jogo deve ser encerrado

    def mostrar_bombas(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] == -1:
                    self.botoes[i][j].config(text="💣", state="disabled")

    def revelar_celula(self, row, col):
        if self.jogo_encerrado or (row, col) in self.bandeiras:
            return

        if self.tempo_inicial is None:
            self.tempo_inicial = time.time()

        if self.tabuleiro[row][col] == -1:
            self.mostrar_bombas()
            self.mostrar_mensagem("Você perdeu!")
            self.jogo_encerrado = True
            self.finalizar_partida()
        else:
            self.revelar_vizinhanca(row, col)
            self.verificar_vitoria()

    def revelar_vizinhanca(self, row, col):
        if row < 0 or row >= self.linhas or col < 0 or col >= self.colunas or (row, col) in self.bandeiras:
            return

        if self.tabuleiro[row][col] == 0:
            self.tabuleiro[row][col] = -2
            self.botoes[row][col].config(text="", state="disabled")
            
            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < self.linhas and 0 <= new_col < self.colunas:
                        self.revelar_vizinhanca(new_row, new_col)
        else:
            self.tabuleiro[row][col] = -2
            self.botoes[row][col].config(text=str(self.tabuleiro[row][col]), state="disabled")

    def marcar_bandeira(self, row, col):
        if self.jogo_encerrado or self.tabuleiro[row][col] != 0:
            return

        if (row, col) in self.bandeiras:
            self.bandeiras.remove((row, col))
            self.botoes[row][col].config(text="", state="normal")
        else:
            self.bandeiras.add((row, col))
            self.botoes[row][col].config(text="🚩")

    def finalizar_partida(self):
        self.tempo_passado = int(time.time() - self.tempo_inicial)

    def verificar_vitoria(self):
        celulas_livres = sum(row.count(0) for row in self.tabuleiro)
        celulas_abertas = sum(row.count(-2) for row in self.tabuleiro)
        if celulas_abertas == celulas_livres:
            self.mostrar_bombas()
            self.jogo_encerrado = True
            self.finalizar_partida()

    def reiniciar_jogo(self):
        self.jogo_encerrado = False
        self.iniciar_jogo(*self.nivel)

if __name__ == "__main__":
    root = tk.Tk()
    game = CampoMinado(root)
    root.mainloop()
