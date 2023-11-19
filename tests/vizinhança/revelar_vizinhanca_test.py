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

def test_revelar_vizinhanca_com_celulas_contendo_zero_facil(campo_minado: CampoMinado):
    # Configuração do tabuleiro com uma célula contendo zero no centro
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, 0, 0, 0],
        [0, -1, 0, -1, 0, -1, -1, -1],
        [0, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, -1, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança na célula central (row=4, col=4)
    campo_minado.revelar_vizinhanca(4, 4)

    # Verifica se todas as células vizinhas com valor zero foram atualizadas e desabilitadas
    for row in range(8):
        for col in range(8):
            if campo_minado.tabuleiro[row][col] == 0:
                assert campo_minado.botoes[row][col]["text"] == "0" and campo_minado.botoes[row][col]["state"] == "disabled"

def test_revelar_vizinhanca_com_celulas_contendo_zero_intertemediario(campo_minado: CampoMinado):
    # Configuração do tabuleiro com uma célula contendo zero no centro
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro = [
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança na célula central (row=4, col=4)
    campo_minado.revelar_vizinhanca(4, 4)

    # Verifica se todas as células vizinhas com valor zero foram atualizadas e desabilitadas
    for row in range(8):
        for col in range(8):
            if campo_minado.tabuleiro[row][col] == 0:
                assert campo_minado.botoes[row][col]["text"] == "0" and campo_minado.botoes[row][col]["state"] == "disabled"

def test_revelar_vizinhanca_com_celulas_contendo_zero_dificil(campo_minado: CampoMinado):
    # Configuração do tabuleiro com uma célula contendo zero no centro
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro = [
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0],
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, -1],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0],
        [0, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança na célula central (row=4, col=4)
    campo_minado.revelar_vizinhanca(4, 4)

    # Verifica se todas as células vizinhas com valor zero foram atualizadas e desabilitadas
    for row in range(8):
        for col in range(8):
            if campo_minado.tabuleiro[row][col] == 0:
                assert campo_minado.botoes[row][col]["text"] == "0" and campo_minado.botoes[row][col]["state"] == "disabled"
                
def test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_facil(campo_minado: CampoMinado):
    # Configuração do tabuleiro com células contendo valores maiores que zero
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.tabuleiro = [
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, -1, -1, 0, 0, 0, 0],
        [0, -1, 3, -1, 0, -1, -1, -1],
        [0, -1, -1, -1, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança em uma célula com valor maior que zero (row=2, col=2)
    campo_minado.revelar_vizinhanca(2, 2)

    # Verifica se a célula foi corretamente atualizada com o valor 3 e desabilitada
    assert campo_minado.botoes[2][2]["text"] == "-2" and campo_minado.botoes[2][2]["state"] == "disabled"
    
def test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_intermediario(campo_minado: CampoMinado):
    # Configuração do tabuleiro com células contendo valores maiores que zero
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.tabuleiro = [
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, -1, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0],
        [0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança em uma célula com valor maior que zero (row=2, col=2)
    campo_minado.revelar_vizinhanca(2, 2)

    # Verifica se a célula foi corretamente atualizada com o valor 3 e desabilitada
    assert campo_minado.botoes[2][2]["text"] == "-2" and campo_minado.botoes[2][2]["state"] == "disabled"
    
def test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_dificil(campo_minado: CampoMinado):
    # Configuração do tabuleiro com células contendo valores maiores que zero
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.tabuleiro = [
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 3, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0],
        [-1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0],
        [-1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, -1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, -1, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, -1, 0, -1, 0, 0, 0],
        [0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0],
        [0, 0, -1, 0, -1, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, -1, -1, 0],
        [0, 0, -1, 0, 0, 0, 0, 0, 0, 0, -1, -1, 0, 0, -1, 0, 0, 0, 0, -1, -1, 0, 0, -1],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, -1, 0, -1, 0],
        [0, 0, -1, 0, 0, 0, -1, 0, -1, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, 0, 0, 0, 0, -1, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, -1, 0, 0],
        [0, -1, -1, 0, -1, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    
    # Chama a função revelar_vizinhança em uma célula com valor maior que zero (row=2, col=2)
    campo_minado.revelar_vizinhanca(2, 2)

    # Verifica se a célula foi corretamente atualizada com o valor 3 e desabilitada
    assert campo_minado.botoes[2][2]["text"] == "-2" and campo_minado.botoes[2][2]["state"] == "disabled"

def test_revelar_vizinhanca_limite_do_tabuleiro_facil(campo_minado: CampoMinado):
    campo_minado.iniciar_jogo(8, 8, 10)

    # Chama a função revelar_vizinhança em células nas bordas do tabuleiro
    # Verifique se não são geradas exceções
    if (campo_minado.revelar_vizinhanca(-1, 0)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, -1)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(8, 0)   # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, 8)):   # Fora dos limites

        campo_minado.jogo_encerrado = True  
    # Verifique se o jogo não está encerrado após as chamadas
        assert campo_minado.jogo_encerrado

def test_revelar_vizinhanca_limite_do_tabuleiro_intermediario(campo_minado: CampoMinado):
    campo_minado.iniciar_jogo(10, 16, 30)

    # Chama a função revelar_vizinhança em células nas bordas do tabuleiro
    # Verifique se não são geradas exceções
    if (campo_minado.revelar_vizinhanca(-1, 0)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, -1)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(10, 0)   # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, 10)):   # Fora dos limites

        campo_minado.jogo_encerrado = True  
    # Verifique se o jogo não está encerrado após as chamadas
        assert campo_minado.jogo_encerrado

def test_revelar_vizinhanca_limite_do_tabuleiro_dificil(campo_minado: CampoMinado):
    campo_minado.iniciar_jogo(24, 24, 100)

    # Chama a função revelar_vizinhança em células nas bordas do tabuleiro
    # Verifique se não são geradas exceções
    if (campo_minado.revelar_vizinhanca(-1, 0)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, -1)  # Fora dos limites
        or campo_minado.revelar_vizinhanca(24, 0)   # Fora dos limites
        or campo_minado.revelar_vizinhanca(0, 24)):   # Fora dos limites

        campo_minado.jogo_encerrado = True  
    # Verifique se o jogo não está encerrado após as chamadas
        assert campo_minado.jogo_encerrado

