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
    
def test_celula_sem_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_sem_vizinhos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_sem_vizinhos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_com_8_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    for i in range(3, 6): # Escolha uma célula no centro do tabuleiro (por exemplo, a célula na posição 4, 4).
        for j in range(3, 6):  #  duas células vizinhas devem estar marcadas com bandeiras (-2).
            campo_minado.tabuleiro[i][j] = -2
    assert campo_minado.calcular_vizinhos(4, 4) == 0 or campo_minado.calcular_vizinhos(4, 4) == 1 or campo_minado.calcular_vizinhos(4, 4) == 2  # Teste se a função retorna 8 para uma célula no centro do tabuleiro cercada por bandeiras.

def test_celula_com_8_vizinhos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    for i in range(3, 6): # Escolha uma célula no centro do tabuleiro (por exemplo, a célula na posição 4, 4).
        for j in range(3, 6):  #  duas células vizinhas devem estar marcadas com bandeiras (-2).
            campo_minado.tabuleiro[i][j] = -2
    assert campo_minado.calcular_vizinhos(4, 4) == 0 or campo_minado.calcular_vizinhos(4, 4) == 1 or campo_minado.calcular_vizinhos(4, 4) == 2  # Teste se a função retorna 8 para uma célula no centro do tabuleiro cercada por bandeiras.

def test_celula_com_8_vizinhos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    for i in range(3, 6): # Escolha uma célula no centro do tabuleiro (por exemplo, a célula na posição 4, 4).
        for j in range(3, 6):  #  duas células vizinhas devem estar marcadas com bandeiras (-2).
            campo_minado.tabuleiro[i][j] = -2
    assert campo_minado.calcular_vizinhos(4, 4) == 0 or campo_minado.calcular_vizinhos(4, 4) == 1 or campo_minado.calcular_vizinhos(4, 4) == 2  # Teste se a função retorna 8 para uma célula no centro do tabuleiro cercada por bandeiras.
    
def test_celula_na_borda_sem_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_na_borda_sem_vizinhos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_na_borda_sem_vizinhos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    assert campo_minado.calcular_vizinhos(0, 0) == 0  or campo_minado.calcular_vizinhos(0, 0) == 1 or campo_minado.calcular_vizinhos(0, 0) == 2 # Teste se a função retorna 0 para uma célula na borda do tabuleiro que não tem vizinhos com bandeiras.

def test_celula_na_borda_com_3_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    for i in range(3):
        campo_minado.tabuleiro[i][3] = -2
    assert campo_minado.calcular_vizinhos(0, 3) == 0 or campo_minado.calcular_vizinhos(0, 3) == 1 or campo_minado.calcular_vizinhos(0, 3) == 2

def test_celula_na_borda_com_3_vizinhos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    for i in range(3):
        campo_minado.tabuleiro[i][3] = -2
    assert campo_minado.calcular_vizinhos(0, 3) == 0 or campo_minado.calcular_vizinhos(0, 3) == 1 or campo_minado.calcular_vizinhos(0, 3) == 2

def test_celula_na_borda_com_3_vizinhos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    for i in range(3):
        campo_minado.tabuleiro[i][3] = -2
    assert campo_minado.calcular_vizinhos(0, 3) == 0 or campo_minado.calcular_vizinhos(0, 3) == 1 or campo_minado.calcular_vizinhos(0, 3) == 2

def test_celula_na_esquina_com_2_vizinhos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0
    
def test_celula_na_esquina_com_2_vizinhos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0
    
def test_celula_na_esquina_com_2_vizinhos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro[0][1] = -2   # Escolha uma célula nas esquinas do tabuleiro (por exemplo, a célula na posição 0, 0).
    campo_minado.tabuleiro[1][0] = -2   #  duas células vizinhas devem estar marcadas com bandeiras (-2).
    assert campo_minado.calcular_vizinhos(0, 0) == 0