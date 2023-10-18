import pytest
from cminado import CampoMinado
import tkinter

@pytest.fixture
def campo_minado():
    root = tkinter.Tk()
    game = CampoMinado(root)
    yield game
    root.destroy()  # Fecha a janela após o teste

@pytest.mark.parametrize("linhas, colunas, bombas, row, col", [(8, 8, 10, 0, 1), 
                                                               (8, 8, 10, 1, 2),
                                                               (8, 8, 10, 4, 5), 
                                                               (8, 8, 10, 3, 6),  
                                                               (8, 8, 10, 2, 3),
                                                               (8, 8, 10, 0, 1), 
                                                               (8, 8, 10, 1, 2),
                                                               (8, 8, 10, 4, 5), 
                                                               (8, 8, 10, 3, 6),  
                                                               (8, 8, 10, 2, 3),
                                                               (8, 8, 10, 0, 1), 
                                                               (8, 8, 10, 1, 2),
                                                               (8, 8, 10, 4, 5), 
                                                               (8, 8, 10, 3, 6),  
                                                               (8, 8, 10, 2, 3)])
def test_clicar_com_bomba_facil(campo_minado, linhas, colunas, bombas, row, col):
    campo_minado.iniciar_jogo(linhas, colunas, bombas)
    campo_minado.clicar(row, col)
    if campo_minado.tabuleiro[row][col] == -1:
        campo_minado.jogo_encerrado = True 
        assert campo_minado.jogo_encerrado 

@pytest.mark.parametrize("linhas, colunas, bombas, row, col", [(10, 16, 30, 0, 1), 
                                                               (10, 16, 30, 1, 2),
                                                               (10, 16, 30, 8, 14), 
                                                               (10, 16, 30, 9, 12), 
                                                               (10, 16, 30, 2, 3),
                                                               (10, 16, 30, 0, 1), 
                                                               (10, 16, 30, 1, 2),
                                                               (10, 16, 30, 8, 14), 
                                                               (10, 16, 30, 9, 12), 
                                                               (10, 16, 30, 2, 3),
                                                               (10, 16, 30, 0, 1), 
                                                               (10, 16, 30, 1, 2),
                                                               (10, 16, 30, 8, 14), 
                                                               (10, 16, 30, 9, 12), 
                                                               (10, 16, 30, 2, 3)])
def test_clicar_com_bomba_intermediario(campo_minado, linhas, colunas, bombas, row, col):
    campo_minado.iniciar_jogo(linhas, colunas, bombas)
    campo_minado.clicar(row, col)
    if campo_minado.tabuleiro[row][col] == -1:
        campo_minado.jogo_encerrado = True 
        assert campo_minado.jogo_encerrado 

@pytest.mark.parametrize("linhas, colunas, bombas, row, col", [(24, 24, 100, 0, 1), 
                                                               (24, 24, 100, 10, 2),
                                                               (24, 24, 100, 21, 14), 
                                                               (24, 24, 100, 9, 22), 
                                                               (24, 24, 100, 2, 3),
                                                               (24, 24, 100, 0, 0), 
                                                               (24, 24, 100, 10, 10),
                                                               (24, 24, 100, 14, 14), 
                                                               (24, 24, 100, 22, 22), 
                                                               (24, 24, 100, 2, 2),
                                                               (24, 24, 100, 1, 1), 
                                                               (24, 24, 100, 2, 2),
                                                               (24, 24, 100, 21, 21), 
                                                               (24, 24, 100, 9, 9), 
                                                               (24, 24, 100, 3, 3)])
def test_clicar_com_bomba_dificil(campo_minado, linhas, colunas, bombas, row, col):
    campo_minado.iniciar_jogo(linhas, colunas, bombas)
    campo_minado.clicar(row, col)
    if campo_minado.tabuleiro[row][col] == -1:
        campo_minado.jogo_encerrado = True 
        assert campo_minado.jogo_encerrado 
