import pytest
from tkinter import Tk
from cminado import CampoMinado 

def mock_askquestion(*args):
    
    if "yes" in args: # Simule a resposta "sim" na caixa de mensagem
        return "yes"
    
    if "no" in args: # Simule a resposta "não" na caixa de mensagem
        return "no"
    return "no"  # Retorno padrão, caso contrário

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

def test_jogo_iniciado_facil(campo_minado):
    linhas, colunas, bombas = 8, 8, 10
    campo_minado.iniciar_jogo(linhas, colunas, bombas)

    assert campo_minado.linhas == linhas and campo_minado.colunas == colunas and campo_minado.bombas == bombas
    
def test_jogo_iniciado_intermediario(campo_minado):
    linhas, colunas, bombas = 10, 16, 30
    campo_minado.iniciar_jogo(linhas, colunas, bombas)
    assert campo_minado.linhas == linhas and campo_minado.colunas == colunas and campo_minado.bombas == bombas
    
def test_jogo_iniciado_dificil(campo_minado):
    linhas, colunas, bombas = 24, 24, 100
    campo_minado.iniciar_jogo(linhas, colunas, bombas)

    assert campo_minado.linhas == linhas and campo_minado.colunas == colunas and campo_minado.bombas == bombas
def test_jogo_encerrado(campo_minado):
    campo_minado.jogo_encerrado = True # Configura o estado do jogo para encerrado  
    assert campo_minado.jogo_encerrado and all(button['state'] == 'disabled'  # Verifica se o jogo está encerrado e todos os botões no tabuleiro estão desabilitados
                                               for row in campo_minado.botoes for button in row)
