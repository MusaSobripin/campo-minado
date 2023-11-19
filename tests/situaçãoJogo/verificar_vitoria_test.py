import pytest
import time
from tkinter import Tk
from cminado import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

def test_verificar_vitoria_jogo_em_andamento_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro = [[0] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado

def test_verificar_vitoria_jogo_em_andamento_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro = [[0] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado

def test_verificar_vitoria_jogo_em_andamento_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro = [[0] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado

def test_verificar_vitoria_vitoria_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado 

def test_verificar_vitoria_vitoria_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado 

def test_verificar_vitoria_vitoria_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado 

def test_verificar_vitoria_derrota_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.tabuleiro[0][0] = 0
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado

def test_verificar_vitoria_derrota_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.tabuleiro[0][0] = 0
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado

def test_verificar_vitoria_derrota_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro = [[-2] * 8 for _ in range(8)]
    campo_minado.tabuleiro[0][0] = 0
    campo_minado.verificar_vitoria()
    assert not campo_minado.jogo_encerrado
