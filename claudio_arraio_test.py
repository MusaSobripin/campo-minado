import datetime
import pytest
from tkinter import Tk
from cnpjto import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

def test_plantar_bombas(campo_minado):
    # Ensure the correct number of bombs are planted
    campo_minado.iniciar_jogo(8, 8, 10)  # Easy level
    bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
    assert bomb_count == 10
    
def test_calcular_vizinhos(campo_minado):
    # Set up a scenario with specific bomb placements and test the calculation
    campo_minado.iniciar_jogo(3, 3, 2)  # No bombs
    campo_minado.tabuleiro = [[-1, 0, 0], 
                              [0, 0, 0], 
                              [0, 0, -1]]

    # Test the cell in the middle
    assert campo_minado.calcular_vizinhos(1, 1) == 2

    # Test a cell with surrounding bombs
    campo_minado.tabuleiro[0][0]

test_cases = [
    # Teste 1
    (
        [
            [-1, -1, -1, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (1, 1),
        5
    ),
    # Teste 2
    (
        [
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (3, 3),
        2
    ),
    # Teste 3
    (
        [
            [-1, -1, 0, 0, 0, 0, 0, 0],
            [0, -1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (0, 2),
        2
    ),
    # Teste 4
    (
        [
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (3, 3),
        3
    ),
    # Teste 5
    (
        [
            [-1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, -1, 0],
            [0, 0, -1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, -1],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ],
        (2, 6),
        2
    ),
]

@pytest.mark.parametrize("tabuleiro, coordenadas, resultado_esperado", test_cases)
def test_celula_com_vizinhos_bomba_em_algumas_direcoes_facil(campo_minado, tabuleiro, coordenadas, resultado_esperado):
    campo_minado.iniciar_jogo(len(tabuleiro), len(tabuleiro[0]), 8)
    campo_minado.tabuleiro = tabuleiro
    x, y = coordenadas
    resultado = campo_minado.calcular_vizinhos(x, y)
    assert resultado == resultado_esperado