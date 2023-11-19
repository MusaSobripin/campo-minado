import pytest
import tkinter as tk
# from pytest_tkinter import TkFixture
from cminado import CampoMinado

@pytest.fixture
def campo_minado():
    root = tk.Tk()
    game = CampoMinado(root)
    yield game
    root.quit()

def test_criacao_do_tabuleiro(campo_minado):
    linhas, colunas = 8, 8
    campo_minado.linhas = linhas
    campo_minado.colunas = colunas
    campo_minado.criar_tabuleiro()

    # Verifique se o frame do tabuleiro foi criado
    assert campo_minado.tabuleiro_frame.winfo_exists() == 1

    # Verifique se o número de botões criados corresponde ao número de linhas e colunas
    assert len(campo_minado.botoes) == linhas
    for linha in campo_minado.botoes:
        assert len(linha) == colunas

    # Verifique se todos os botões foram criados
    for i in range(linhas):
        for j in range(colunas):
            assert campo_minado.botoes[i][j].winfo_exists() == 1

def test_eventos_de_clique_facil(campo_minado):
    campo_minado.linhas = 8
    campo_minado.colunas = 8
    campo_minado.criar_tabuleiro()

    # Função auxiliar para simular um clique com o botão esquerdo
    def simulate_left_click(button):
        button.event_generate("<Button-1>")

    # Função auxiliar para simular um clique com o botão direito
    def simulate_right_click(button):
        button.event_generate("<Button-3>")

    # Verifique se os eventos de clique ("<Button-1>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_left_click(button) # Simule um clique com o botão esquerdo

    # Verifique se os eventos de clique ("<Button-3>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_right_click(button) # Simule um clique com o botão direito

def test_eventos_de_clique_intermediario(campo_minado):
    campo_minado.linhas = 10
    campo_minado.colunas = 16
    campo_minado.criar_tabuleiro()

    # Função auxiliar para simular um clique com o botão esquerdo
    def simulate_left_click(button):
        button.event_generate("<Button-1>")

    # Função auxiliar para simular um clique com o botão direito
    def simulate_right_click(button):
        button.event_generate("<Button-3>")

    # Verifique se os eventos de clique ("<Button-1>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_left_click(button) # Simule um clique com o botão esquerdo

    # Verifique se os eventos de clique ("<Button-3>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_right_click(button) # Simule um clique com o botão direito

def test_eventos_de_clique_dificil(campo_minado):
    campo_minado.linhas = 24
    campo_minado.colunas = 24
    campo_minado.criar_tabuleiro()

    # Função auxiliar para simular um clique com o botão esquerdo
    def simulate_left_click(button):
        button.event_generate("<Button-1>")

    # Função auxiliar para simular um clique com o botão direito
    def simulate_right_click(button):
        button.event_generate("<Button-3>")

    # Verifique se os eventos de clique ("<Button-1>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_left_click(button) # Simule um clique com o botão esquerdo

    # Verifique se os eventos de clique ("<Button-3>") estão configurados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]
            simulate_right_click(button) # Simule um clique com o botão direito

def test_vinculacao_de_eventos():
    root = tk.Tk()
    campo_minado = CampoMinado(root)

    # Suponha que a função criar_tabuleiro seja chamada para configurar os botões
    campo_minado.criar_tabuleiro()

    # Verifique se os eventos de clique ("<Button-1>") estão vinculados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]

            # Crie um evento simulado de clique do botão 1
            event = tk.Event()
            event.num = 1

            # Chame manualmente o método que trata o evento de clique do botão
            campo_minado.clicar(i, j, event)

            # Insira a verificação se o método self.clicar foi chamado corretamente

    # Verifique se os eventos de clique ("<Button-3>") estão vinculados corretamente
    for i in range(campo_minado.linhas):
        for j in range(campo_minado.colunas):
            button = campo_minado.botoes[i][j]

            # Crie um evento simulado de clique do botão 3
            event = tk.Event()
            event.num = 3

            # Chame manualmente o método que trata o evento de clique do botão
            campo_minado.marcar_bandeira(i, j, event)

            # Insira a verificação se o método self.marcar_bandeira foi chamado corretamente


