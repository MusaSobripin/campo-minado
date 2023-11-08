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
        self.bandeiras_marcadas = 0
        self.limite_bandeiras = 0
        self.placar_bombas = tk.Label(root, text="Bombas Restantes: 0")
        self.placar_tempo = tk.Label(root, text="Tempo: 0s")

        self.tempo_inicial = None
        self.tempo_passado = 0
        self.timer_label = tk.Label(root)
        self.timer_label.pack()

        self.tabuleiro_frame = None

        self.partidas_jogadas = []

        self.criar_menu_niveis()
        self.criar_botao_tutorial()
        self.atualizar_placar_bombas()

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
        if self.jogo_encerrado:
            self.reiniciar_jogo()
        self.nivel = (linhas, colunas, bombas)
        self.linhas = linhas
        self.colunas = colunas
        self.bombas_posicoes = set()
        self.bombas = bombas
        self.jogo_encerrado = False
        self.tempo_inicial = None
        self.tempo_passado = 0
        self.bandeiras_marcadas = 0  # Reiniciar o contador de bandeiras marcadas

        if self.tabuleiro_frame:
            self.tabuleiro_frame.destroy()

        self.criar_tabuleiro()
        self.plantar_bombas()
        self.limite_bandeiras = self.bombas  # Define o limite de bandeiras com base na quantidade de bombas
    
    def atualizar_placar_bombas(self):
        bombas_restantes = self.bombas - self.bandeiras_marcadas
        self.placar_bombas.config(text=f"Bombas Restantes: {bombas_restantes}")
        self.placar_bombas.pack()

    def atualizar_placar_tempo(self):
        if not self.jogo_encerrado:
            self.tempo_passado = int(time.time() - self.tempo_inicial)
            self.placar_tempo.config(text=f"⏰: {self.tempo_passado}s")
            self.root.after(1000, self.atualizar_placar_tempo)
        else:
            self.placar_tempo.pack()
    def criar_botao_tutorial(self):
        tutorial_button = tk.Button(self.root, text="Tutorial", command=self.exibir_tutorial)
        tutorial_button.pack()

    def exibir_tutorial(self):
        tutorial = """
        Como jogar Campo Minado:
        
        1. Clique com o botão esquerdo do mouse para abrir uma célula.
        2. Clique com o botão direito do mouse para marcar ou desmarcar uma bandeira.
        3. Se clicar em uma célula com uma bomba, o jogo termina.
        4. O objetivo é abrir todas as células que não contêm bombas.
        5. Se todas as células sem bombas forem abertas, você vence o jogo.
        
        Boa sorte!
        """
        tkinter.messagebox.showinfo("Tutorial", tutorial)
    
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

        self.iniciar_timer()
        self.atualizar_placar_bombas()

    def iniciar_timer(self):
        self.tempo_inicial = time.time()
        self.atualizar_placar_tempo()
    
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
        if self.jogo_encerrado or self.tabuleiro[row][col] == -2 or self.botoes[row][col]["text"] == "🚩":
            return

        if self.tempo_inicial is None:
            self.iniciar_timer()

        if self.tabuleiro[row][col] == -1:
            self.mostrar_bombas()
            self.mostrar_mensagem("Você perdeu!")
            self.jogo_encerrado = True
            self.finalizar_partida()
        else:
            self.revelar_celula(row, col)
            self.verificar_vitoria("Parabéns, você venceu!!!")

    def mostrar_mensagem(self, mensagem):
        resposta = tkinter.messagebox.askquestion("Resultado", mensagem + f"\nDeseja jogar novamente?")
        if resposta == "yes":
            self.iniciar_jogo(*self.nivel)
        else:
            partida = {
                "nivel": self.nivel,
                "tempo": self.tempo_passado,
                "resultado": "Vitória" if not self.jogo_encerrado else "Derrota"
            }
            self.partidas_jogadas.append(partida)

            self.root.quit()
            raise SystemExit

    def mostrar_bombas(self):
        for i in range(self.linhas):
            for j in range(self.colunas):
                if self.tabuleiro[i][j] == -1:
                    self.botoes[i][j].config(text="💣", state="disabled")

    def calcular_vizinhos(self, x, y):
        bomb_count = 0

        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= x + i < self.linhas and 0 <= y + j < self.colunas:
                    if self.tabuleiro[x + i][y + j] == -1:
                        bomb_count += 1

        # Se a célula em (x, y) tiver uma bomba, subtrair 1 para evitar contar a própria célula
        try:
            if self.tabuleiro[x][y] == -1:
                bomb_count -= 1
        except: IndexError

        return bomb_count

    def revelar_celula(self, row, col):
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
            bomb_count = self.calcular_vizinhos(row, col)
            if bomb_count > 0:
                self.botoes[row][col].config(text=str(bomb_count), state="disabled")
            else:
                self.revelar_vizinhanca(row, col)
            self.tabuleiro[row][col] = -2
            self.verificar_vitoria()

    def revelar_vizinhanca(self, row, col):
        if row < 0 or row >= self.linhas or col < 0 or col >= self.colunas or self.tabuleiro[row][col] == -2:
            return

        if self.tabuleiro[row][col] == 0:
            self.tabuleiro[row][col] = -2
            self.botoes[row][col].config(text="0", state="disabled")

            for dr in [-1, 0, 1]:
                for dc in [-1, 0, 1]:
                    if dr == 0 and dc == 0:
                        continue
                    new_row, new_col = row + dr, col + dc
                    if 0 <= new_row < self.linhas and 0 <= new_col < self.colunas:
                        if self.tabuleiro[new_row][new_col] == 0:
                            self.revelar_vizinhanca(new_row, new_col)
                        elif self.tabuleiro[new_row][new_col] > 0:
                            self.botoes[new_row][new_col].config(text=str(self.tabuleiro[new_row][new_col]), state="disabled")
        else:
            self.tabuleiro[row][col] = -2
            self.botoes[row][col].config(text=str(self.tabuleiro[row][col]), state="disabled")

    def marcar_bandeira(self, row, col):
        if self.jogo_encerrado or self.tabuleiro[row][col] == -2:
            return
        if self.botoes[row][col]["text"] == "":
            self.botoes[row][col].config(text="🚩")
            self.bandeiras_marcadas -= 1
        elif self.botoes[row][col]["text"] == "🚩":
            self.botoes[row][col].config(text="")
            self.bandeiras_marcadas += 1
        else:
            # Verificar se o limite de bandeiras foi atingido
            if self.bandeiras_marcadas < self.limite_bandeiras:
                self.botoes[row][col].config(text="🚩")
                self.bandeiras_marcadas += 1  # Incrementar o contador de bandeiras marcadas

    
    def verificar_vitoria(self, mensagem="Parabéns, você ganhou!!!"):
        celulas_livres = sum(row.count(0) for row in self.tabuleiro)
        celulas_abertas = sum(row.count(-2) for row in self.tabuleiro)
        if celulas_abertas == celulas_livres:
            self.mostrar_bombas()
            self.jogo_encerrado = True
            self.finalizar_partida(mensagem)

    
    def finalizar_partida(self):
        self.tempo_passado = int(time.time() - self.tempo_inicial)

    def mostrar_historico(self):
        if self.partidas_jogadas:
            historico = "\n".join([f"Nível: {partida['nivel']}, Tempo: {partida['tempo']} segundos, Resultado: {partida['resultado']}" for partida in self.partidas_jogadas])
            tkinter.messagebox.showinfo("Histórico de Partidas", historico)
        else:
            tkinter.messagebox.showinfo("Histórico de Partidas", "Nenhuma partida jogada ainda.")

    def reiniciar_jogo(self):
        self.jogo_encerrado = False
        self.iniciar_jogo(*self.nivel)

if __name__ == "__main__":
    root = tk.Tk()
    game = CampoMinado(root)

    historico_button = tk.Button(root, text="Histórico de Partidas", command=game.mostrar_historico)
    historico_button.pack()

    root.mainloop()
