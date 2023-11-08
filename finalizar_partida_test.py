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
    
def test_finalizar_partida_tempo_passado_facil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 10 segundos atrás)
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tempo_inicial = time.time() - 10
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 10 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_intermediario(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 10 segundos atrás)
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tempo_inicial = time.time() - 10
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 10 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_dificil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 10 segundos atrás)
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tempo_inicial = time.time() - 10
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 10 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_zero_facil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial igual ao tempo atual (tempo zero)
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tempo_inicial = time.time()
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 0 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_zero_intermediario(campo_minado):
    # Inicialize o jogo e defina um tempo inicial igual ao tempo atual (tempo zero)
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tempo_inicial = time.time()
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 0 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_zero_dificil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial igual ao tempo atual (tempo zero)
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tempo_inicial = time.time()
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 0 # verificar se o tempo passado é igual a 0

def test_finalizar_partida_tempo_passado_arredondado_facil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 15.49 segundos atrás)
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tempo_inicial = time.time() - 15.49
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 15 # verificar se o tempo passado é igual a 15 (arredondado para int)

def test_finalizar_partida_tempo_passado_arredondado_intermediario(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 15.49 segundos atrás)
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tempo_inicial = time.time() - 15.49
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 15 # verificar se o tempo passado é igual a 15 (arredondado para int)
 
def test_finalizar_partida_tempo_passado_arredondado_dificil(campo_minado):
    # Inicialize o jogo e defina um tempo inicial fictício (por exemplo, 15.49 segundos atrás)
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tempo_inicial = time.time() - 15.49
    campo_minado.finalizar_partida()
    assert campo_minado.tempo_passado == 15 # verificar se o tempo passado é igual a 15 (arredondado para int)
    