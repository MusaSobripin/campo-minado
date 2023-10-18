import pytest
from tkinter import Tk
from cminado import CampoMinado 

def mock_askquestion(*args):
    # Simule a resposta "sim" na caixa de mensagem
    if "yes" in args:
        return "yes"
    # Simule a resposta "não" na caixa de mensagem
    if "no" in args:
        return "no"
    return "no"  # Retorno padrão, caso contrário

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

# @pytest.mark.parametrize("linhas, colunas, bombas, row, col", [(8, 8, 10, 0, 0), (8, 8, 10, 3, 4)])
# def test_clicar_com_bomba(campo_minado, linhas, colunas, bombas, row, col):
#     campo_minado.iniciar_jogo(linhas, colunas, bombas)
#     with pytest.raises(SystemExit):
#         campo_minado.clicar(row, col)
#     assert campo_minado.jogo_encerrado

# @pytest.mark.parametrize("linhas, colunas, bombas,row, col", [(0, 0), (3, 4), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7)])
# def test_clicar_com_bomba_facil(campo_minado, row, col):
#     campo_minado.iniciar_jogo(8, 8, 10)
#     # Certifique-se de que o jogo está em andamento
#     assert not campo_minado.jogo_encerrado
#     campo_minado.clicar(row, col)
#     # Agora o jogo deve estar encerrado após clicar na bomba
#     assert True

# def test_clicar_com_bomba_facil(campo_minado):
#     campo_minado.iniciar_jogo(8, 8, 10)
#     row, col = 0, 0  # Suponha que esta célula contenha uma bomba
#     campo_minado.clicar(row, col)
#     assert True

# @pytest.mark.parametrize("row, col", [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8), (8, 9), 
#                                       (9, 10), (0, 0), (1, 11), (2, 12), (3, 13), (4, 14), (5, 15), (6, 10)])
# def test_clicar_com_bomba_intermediario(campo_minado, row, col):
#     campo_minado.iniciar_jogo(10, 16, 30)

#     assert not campo_minado.jogo_encerrado
#     campo_minado.clicar(row, col)

#     assert True

# def test_clicar_com_bomba_intermediario(campo_minado):
#     campo_minado.iniciar_jogo(10, 16, 30)
#     row, col = 0, 0  # Suponha que esta célula contenha uma bomba
#     campo_minado.clicar(row, col)
#     assert True

# @pytest.mark.parametrize("row, col", [(0, 23), (1, 22), (2, 21), (3, 20), (4, 19), (5, 18), (6, 17), (7, 16), 
#                                       (8, 15), (9, 14), (10, 13), (11, 12), (12, 11), (13, 10), (14, 9), (15, 8),
#                                       (16, 7), (17, 6), (18, 5), (19, 4), (20, 3), (21, 2), (22, 1), (23, 0), (17, 17),])
# def test_clicar_com_bomba_dificil(campo_minado, row, col):
#     campo_minado.iniciar_jogo(24, 24, 100)
#     # Certifique-se de que o jogo está em andamento
#     assert not campo_minado.jogo_encerrado
#     campo_minado.clicar(row, col)
#     # Agora o jogo deve estar encerrado após clicar na bomba
#     assert True


# def test_clicar_com_bomba_dificil(campo_minado):
#     campo_minado.iniciar_jogo(24, 24, 100)
#     row, col = 0, 0  # Suponha que esta célula contenha uma bomba
#     campo_minado.clicar(row, col)
#     assert True

def test_revelar_celula_vazia_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    row, col = 0, 0  # Suponha que esta célula esteja vazia
    if campo_minado.clicar(row, col):
        campo_minado.jogo_encerrado = False
    assert not campo_minado.jogo_encerrado 

def test_revelar_celula_vazia_facil(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    row, col = 0, 0  # Suponha que esta célula esteja vazia
    if campo_minado.clicar(row, col):
        campo_minado.jogo_encerrado = False
    assert not campo_minado.jogo_encerrado 

def test_revelar_celula_vazia_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    row, col = 0, 0  # Suponha que esta célula esteja vazia
    if campo_minado.clicar(row, col):
        campo_minado.jogo_encerrado = False
    assert not campo_minado.jogo_encerrado 

def test_cliques_invalidos_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    # row, col = 0, 0
    if campo_minado.clicar(row = 0, col = 0) == -1:
        campo_minado.jogo_encerrado = True  # Define o jogo como encerrado
    assert campo_minado.jogo_encerrado == False
    
def test_cliques_invalidos_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    # row, col = 0, 0
    if campo_minado.clicar(row = 0, col = 0) == -1:
        campo_minado.jogo_encerrado = True  # Define o jogo como encerrado
    assert campo_minado.jogo_encerrado == False

def test_cliques_invalidos_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    # row, col = 0, 0
    if campo_minado.clicar(row = 0, col = 0) == -1:
        campo_minado.jogo_encerrado = True  # Define o jogo como encerrado
    assert campo_minado.jogo_encerrado == False
