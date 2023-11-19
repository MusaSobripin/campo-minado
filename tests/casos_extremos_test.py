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

def test_tamanho_minimo_do_tabuleiro(campo_minado):
    campo_minado.iniciar_jogo(1, 1, 0)
    resultado = campo_minado.calcular_vizinhos(0, 0)
    assert resultado == 0, "O tabuleiro de tamanho mínimo deve ter 0 vizinhos bomba."

def test_tamanho_maximo_do_tabuleiro(campo_minado):
    # Ajuste isso para o tamanho máximo do tabuleiro, se houver um limite.
    # Por exemplo, se o limite for 100x100:
    campo_minado.iniciar_jogo(100, 100, 0)
    resultado = campo_minado.calcular_vizinhos(50, 50)  # Coordenadas no centro do tabuleiro
    assert resultado == 0, "O tabuleiro de tamanho máximo deve ter 0 vizinhos bomba."

def test_coordenadas_extremas_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)

    # Teste com coordenadas mínimas (0, 0)
    resultado_minimo = campo_minado.calcular_vizinhos(0, 0)
    assert resultado_minimo >= 0, "As coordenadas mínimas não devem causar erros."

    # Ajuste isso para as coordenadas máximas com base no tamanho do tabuleiro.
    # Por exemplo, se o tabuleiro for 8x8:
    tamanho_maximo = 7
    resultado_maximo = campo_minado.calcular_vizinhos(tamanho_maximo, tamanho_maximo)
    assert resultado_maximo >= 0, "As coordenadas máximas não devem causar erros."

def test_coordenadas_extremas_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)

    # Teste com coordenadas mínimas (0, 0)
    resultado_minimo = campo_minado.calcular_vizinhos(0, 0)
    assert resultado_minimo >= 0, "As coordenadas mínimas não devem causar erros."

    # Ajuste isso para as coordenadas máximas com base no tamanho do tabuleiro.
    # Por exemplo, se o tabuleiro for 10x16:
    tamanho_maximo_x = 9
    tamanho_maximo_y = 15
    resultado_maximo = campo_minado.calcular_vizinhos(tamanho_maximo_x, tamanho_maximo_y)
    assert resultado_maximo >= 0, "As coordenadas máximas não devem causar erros."
    
def test_coordenadas_extremas_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)

    # Teste com coordenadas mínimas (0, 0)
    resultado_minimo = campo_minado.calcular_vizinhos(0, 0)
    assert resultado_minimo >= 0, "As coordenadas mínimas não devem causar erros."

    # Ajuste isso para as coordenadas máximas com base no tamanho do tabuleiro.
    # Por exemplo, se o tabuleiro for 10x16:
    tamanho_maximo_x = 23
    tamanho_maximo_y = 23
    resultado_maximo = campo_minado.calcular_vizinhos(tamanho_maximo_x, tamanho_maximo_y)
    assert resultado_maximo >= 0, "As coordenadas máximas não devem causar erros."