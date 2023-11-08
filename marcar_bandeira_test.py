import pytest
from tkinter import Tk
from cminado import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

def test_marcar_bandeira_em_celula_sem_bandeira_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    row, col = 0, 0     # Escolha uma célula sem bandeira (por exemplo, a célula na posição 0, 0)
    campo_minado.tabuleiro[row][col] != -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩'
    
def test_marcar_bandeira_em_celula_sem_bandeira_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    row, col = 0, 0     # Escolha uma célula sem bandeira (por exemplo, a célula na posição 0, 0)
    campo_minado.tabuleiro[row][col] != -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩'
    
def test_marcar_bandeira_em_celula_sem_bandeira_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    row, col = 0, 0     # Escolha uma célula sem bandeira (por exemplo, a célula na posição 0, 0)
    campo_minado.tabuleiro[row][col] != -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩'

def test_desmarcar_bandeira_em_celula_marcada_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    row, col = 0, 0     # Escolha uma célula e marque-a com uma bandeira
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.tabuleiro[row][col] == -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == "" and campo_minado.botoes[row][col]["state"] == "normal"    

def test_desmarcar_bandeira_em_celula_marcada_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    row, col = 0, 0     # Escolha uma célula e marque-a com uma bandeira
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.tabuleiro[row][col] == -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == "" and campo_minado.botoes[row][col]["state"] == "normal"    

def test_desmarcar_bandeira_em_celula_marcada_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    row, col = 0, 0     # Escolha uma célula e marque-a com uma bandeira
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.tabuleiro[row][col] == -2
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == "" and campo_minado.botoes[row][col]["state"] == "normal"    

def test_marcar_bandeira_em_celula_com_bomba_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    row, col = 0, 0  # Supondo que esta célula contenha uma bomba
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩' and campo_minado.botoes[row][col]["state"] == "normal"

def test_marcar_bandeira_em_celula_com_bomba_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    row, col = 0, 0  # Supondo que esta célula contenha uma bomba
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩' and campo_minado.botoes[row][col]["state"] == "normal"

def test_marcar_bandeira_em_celula_com_bomba_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    row, col = 0, 0  # Supondo que esta célula contenha uma bomba
    campo_minado.marcar_bandeira(row, col)
    assert campo_minado.botoes[row][col].cget("text") == '🚩' and campo_minado.botoes[row][col]["state"] == "normal"
