import datetime
import pytest
import tkinter as tk
from main.cnpjto import CampoMinado  # Substitua 'your_module' pelo nome real do seu módulo

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root, 8, 8, 1, None)
    yield game
    root.quit()
    
def test_celula_sem_vizinhos_bomba():
    tabuleiro = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
    x, y = 1, 1
    resultado = calcular_vizinhos(tabuleiro, x, y)
    assert resultado == 0, "A célula deve ter 0 vizinhos bomba."

def test_celula_com_vizinhos_bomba_em_todas_as_direcoes():
    tabuleiro = [
        [-1, -1, -1],
        [-1, 0, -1],
        [-1, -1, -1]
    ]
    x, y = 1, 1
    resultado = calcular_vizinhos(tabuleiro, x, y)
    assert resultado == 8, "A célula deve ter 8 vizinhos bomba."
