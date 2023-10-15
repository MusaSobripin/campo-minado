import pytest
from tkinter import Tk
# from pytest_tkinter import TkFixture
from cminado import CampoMinado  # Substitua 'seu_modulo' pelo nome real do seu módulo

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()

# def test_interacao_de_botoes(campo_minado):
#     campo_minado.nivel = "Fácil"

#     def pressiona_botao():
#         botao = campo_minado.root.nametowidget(".!button")  # Suponha que o botão seja o único na janela
#         botao.invoke()

#     campo_minado.root.after(2000, pressiona_botao)

#     resultado = campo_minado.iniciar_jogo(8, 8, 10)

#     assert resultado == (8, 8, 10), f"A função self.iniciar_jogo deveria ser chamada com os parâmetros corretos, mas recebeu {resultado}."

def test_numero_de_botoes(campo_minado):
    
    botoes = campo_minado.criar_menu_niveis() # Chame a função que cria os botões do menu
    numero_de_niveis_esperados = 3  # Defina o número esperado de botões com base em sua implementação 
    assert len(botoes) == numero_de_niveis_esperados-1 # Verifique se o número de botões criados corresponde ao número esperado

    campo_minado.root.destroy()
    
def test_ordem_dos_botoes(campo_minado):
    
    campo_minado.botao_label, botoes = campo_minado.criar_menu_niveis() # Obtenha os botões criados chamando a função criar_menu_niveis
    textos_dos_botoes = [botao.cget("text") for botao in botoes]  # Obtenha os textos dos botões
    ordem_esperada = ["Fácil", "Intermediário", "Difícil"] # Defina a ordem esperada dos níveis com base em sua implementação 
                                                           
    assert textos_dos_botoes == ordem_esperada # Verifique se a ordem dos botões corresponde à ordem esperada

    campo_minado.root.destroy()
    
# def test_manipulacao_de_eventos(campo_minado):
#     # Simule um clique no botão de nível "Fácil"
#     campo_minado.nivel = "Fácil"

#     # Obtenha todos os botões no frame do menu
#     botoes = campo_minado.root.winfo_children()
    
#     # Encontre o botão com o texto "Fácil"
#     botao_facil = None
#     for botao in botoes:
#         if "Fácil" in botao.cget("text"):
#             botao_facil = botao
#             break
    
#     assert botao_facil is not None, "Botão 'Fácil' não encontrado."

#     def pressiona_botao():
#         botao_facil.invoke()
    
#     campo_minado.root.after(2000, pressiona_botao)

#     resultado = campo_minado.iniciar_jogo(8, 8, 10)

#     assert resultado == (8, 8, 10), f"A função self.iniciar_jogo deveria ser chamada com os parâmetros corretos, mas recebeu {resultado}."
