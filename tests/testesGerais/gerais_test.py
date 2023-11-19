# import pytest
# import tkinter as tk
# from cminado import CampoMinado  # Supondo que o código do CampoMinado esteja em um arquivo campo_minado.py

# @pytest.fixture
# def campo_minado():
#     root = tk.Tk()
#     game = CampoMinado(root)
#     yield game
#     root.destroy()

# def test_iniciar_novo_jogo(campo_minado):
#     # Verifica se o nível, tamanho do tabuleiro e número de bombas estão corretos
#     assert campo_minado.nivel is not None
#     linhas, colunas, bombas = campo_minado.nivel
#     assert linhas == campo_minado.linhas
#     assert colunas == campo_minado.colunas
#     assert bombas == campo_minado.bombas

#     # Garante que o tabuleiro esteja vazio no início do jogo
#     for row in campo_minado.tabuleiro:
#         assert all(cell == 0 for cell in row)

# def test_plantar_bombas(campo_minado):
#     campo_minado.iniciar_jogo(8, 8, 10)

#     # Confirmar que o número correto de bombas foi plantado
#     bomb_count = sum(row.count(-1) for row in campo_minado.tabuleiro)
#     assert bomb_count == 10

# def test_clicar_em_celula(campo_minado):
#     campo_minado.iniciar_jogo(8, 8, 10)

#     # Verificar se o jogador pode clicar em uma célula vazia
#     campo_minado.clicar(0, 0)
#     assert campo_minado.tabuleiro[0][0] == -2  # A célula foi revelada

#     # Certificar-se de que, se uma bomba for clicada, o jogo termina
#     with pytest.raises(SystemExit):
#         campo_minado.clicar(1, 1)

# def test_marcar_e_desmarcar_bandeiras(campo_minado):
#     campo_minado.iniciar_jogo(8, 8, 10)

#     # Marcar uma bandeira em uma célula
#     campo_minado.marcar_bandeira(0, 0)
#     assert campo_minado.tabuleiro[0][0] == -2  # A célula está marcada com uma bandeira

#     # Desmarcar a bandeira
#     campo_minado.marcar_bandeira(0, 0)
#     assert campo_minado.tabuleiro[0][0] == 0  # A bandeira foi removida

#     # Verificar que o número de bandeiras marcadas é contado corretamente
#     bandeiras_restantes = campo_minado.bombas - campo_minado.contar_vizinhos(0, 1)
#     assert bandeiras_restantes == campo_minado.bandeiras_marcadas
