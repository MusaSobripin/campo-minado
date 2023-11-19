import pytest
from cminado import CampoMinado
import tkinter

@pytest.fixture
def campo_minado():
    root = tkinter.Tk()
    game = CampoMinado(root)
    yield game
    root.destroy() 

def test_dimensoes_nivel_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    assert campo_minado.linhas == 8 and campo_minado.colunas == 8 and campo_minado.bombas == 10

def test_dimensoes_nivel_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    assert campo_minado.linhas == 10 and campo_minado.colunas == 16 and campo_minado.bombas == 30

def test_dimensoes_nivel_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    assert campo_minado.linhas == 24 and campo_minado.colunas == 24 and campo_minado.bombas == 100
