import pytest
import time
import timeit
from tkinter import Tk
from cnpjto import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()
    
def test_desempenho_tabuleiro_pequeno(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    x, y = 3, 3
    tempo_inicio = time.time()
    campo_minado.calcular_vizinhos(x, y)
    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    assert tempo_execucao < 1, "Tempo de execução para tabuleiro pequeno é maior que 1 segundo."

def test_desempenho_time_tabuleiro_pequeno(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    x, y = 3, 3

    def calcular_vizinhos():
        campo_minado.calcular_vizinhos(x, y)

    tempo_execucao = timeit.timeit(calcular_vizinhos, number=1000)  # Número de execuções para obter uma medição precisa
    assert tempo_execucao < 1, "Tempo de execução para tabuleiro pequeno é maior que 1 segundo."


def test_desempenho_tabuleiro_medio(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    x, y = 8, 8
    tempo_inicio = time.time()
    campo_minado.calcular_vizinhos(x, y)
    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    assert tempo_execucao < 1, "Tempo de execução para tabuleiro médio é maior que 1 segundo."

def test_desempenho_tabuleiro_grande(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    x, y = 16, 16
    tempo_inicio = time.time()
    campo_minado.calcular_vizinhos(x, y)
    tempo_fim = time.time()
    tempo_execucao = tempo_fim - tempo_inicio
    assert tempo_execucao < 1, "Tempo de execução para tabuleiro grande é maior que 1 segundo."

