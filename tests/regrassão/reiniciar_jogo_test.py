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

def test_reiniciar_jogo_jogo_encerrado_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.jogo_encerrado = True
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado

def test_reiniciar_jogo_jogo_encerrado_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.jogo_encerrado = True
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado

def test_reiniciar_jogo_jogo_encerrado_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.jogo_encerrado = True
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado

def test_reiniciar_jogo_valores_padrao_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.jogo_encerrado = True
    campo_minado.nivel = (8, 8, 10)
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado and campo_minado.nivel == (8, 8, 10)

def test_reiniciar_jogo_valores_padrao_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.jogo_encerrado = True
    campo_minado.nivel = (10, 16, 30)
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado and campo_minado.nivel == (10, 16, 30)

def test_reiniciar_jogo_valores_padrao_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.jogo_encerrado = True
    campo_minado.nivel = (24, 24, 100)
    campo_minado.reiniciar_jogo()
    assert not campo_minado.jogo_encerrado and campo_minado.nivel == (24, 24, 100)
