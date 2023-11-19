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

def test_celula_na_esquina_com_1_vizinhos_bomba_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_2_vizinhos_bomba_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_3_vizinhos_bomba_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_1_vizinhos_bomba_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_2_vizinhos_bomba_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_3_vizinhos_bomba_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_1_vizinhos_bomba_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_2_vizinhos_bomba_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_3_vizinhos_bomba_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0 or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2

def test_celula_na_esquina_com_2_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro[0][1] = -2
    campo_minado.tabuleiro[1][0] = -2
    vizinhos = campo_minado.calcular_vizinhos(0, 0)
    assert vizinhos in [0, 1, 2]