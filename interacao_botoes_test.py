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

def test_interacao_de_botoes_facil(campo_minado):
    # Defina o nível desejado
    campo_minado.iniciar_jogo (8, 8, 10)
    campo_minado.nivel_desejado = "Fácil"
    
    def pressiona_botao():
        campo_minado.botao_texto = 'Fácil'  # Use o nível desejado
        botao_encontrado = None
    
        # Iterar pelos botões em busca do botão com o texto desejado
        for widget in campo_minado.root.winfo_children():
            if widget.cget("text") == campo_minado.botao_texto:
                botao_encontrado = widget
                break
    
        if botao_encontrado:
            botao_encontrado.invoke()
        else:
            raise AssertionError(f"Botão com texto '{campo_minado.botao_texto}' não encontrado na interface.")
    
    campo_minado.label, campo_minado.buttons = campo_minado.criar_menu_niveis()
    campo_minado.root.update_idletasks()  # Garante que a interface esteja atualizada
    
    campo_minado.root.after(2000, pressiona_botao)
    
    # Verifique se a função iniciar_jogo foi chamada com os parâmetros corretos
    nivel_esperado = (8, 8, 10)
    resultado = campo_minado.nivel
    
    # Verifique se o nível selecionado corresponde ao esperado
    assert resultado == nivel_esperado, f"O nível selecionado deveria ser '{nivel_esperado}', mas foi '{resultado}'."

def test_interacao_de_botoes_intermediario(campo_minado):
    # Defina o nível desejado
    campo_minado.iniciar_jogo (10, 16, 30)
    campo_minado.nivel_desejado = "Intermediário"
    
    def pressiona_botao():
        campo_minado.botao_texto = 'Intermediário'  # Use o nível desejado
        botao_encontrado = None
    
        # Iterar pelos botões em busca do botão com o texto desejado
        for widget in campo_minado.root.winfo_children():
            if widget.cget("text") == campo_minado.botao_texto:
                botao_encontrado = widget
                break
    
        if botao_encontrado:
            botao_encontrado.invoke()
        else:
            raise AssertionError(f"Botão com texto '{campo_minado.botao_texto}' não encontrado na interface.")
    
    campo_minado.label, campo_minado.buttons = campo_minado.criar_menu_niveis()
    campo_minado.root.update_idletasks()  # Garante que a interface esteja atualizada
    
    campo_minado.root.after(2000, pressiona_botao)
    
    # Verifique se a função iniciar_jogo foi chamada com os parâmetros corretos
    nivel_esperado = (10, 16, 30)
    resultado = campo_minado.nivel
    
    # Verifique se o nível selecionado corresponde ao esperado
    assert resultado == nivel_esperado, f"O nível selecionado deveria ser '{nivel_esperado}', mas foi '{resultado}'."

def test_interacao_de_botoes_dificil(campo_minado):
    # Defina o nível desejado
    campo_minado.iniciar_jogo (24, 24, 100)
    campo_minado.nivel_desejado = "Difícil"
    
    def pressiona_botao():
        campo_minado.botao_texto = 'Difícil'  # Use o nível desejado
        botao_encontrado = None
    
        # Iterar pelos botões em busca do botão com o texto desejado
        for widget in campo_minado.root.winfo_children():
            if widget.cget("text") == campo_minado.botao_texto:
                botao_encontrado = widget
                break
    
        if botao_encontrado:
            botao_encontrado.invoke()
        else:
            raise AssertionError(f"Botão com texto '{campo_minado.botao_texto}' não encontrado na interface.")
    
    campo_minado.label, campo_minado.buttons = campo_minado.criar_menu_niveis()
    campo_minado.root.update_idletasks()  # Garante que a interface esteja atualizada
    
    campo_minado.root.after(2000, pressiona_botao)
    
    # Verifique se a função iniciar_jogo foi chamada com os parâmetros corretos
    nivel_esperado = (24, 24, 100)
    resultado = campo_minado.nivel
    
    # Verifique se o nível selecionado corresponde ao esperado
    assert resultado == nivel_esperado, f"O nível selecionado deveria ser '{nivel_esperado}', mas foi '{resultado}'."

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
    
# def test_manipulacao_de_eventos_facil(campo_minado):
#     campo_minado.iniciar_jogo(8, 8, 10)

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

#     # Espere até que o jogo seja iniciado
#     campo_minado.root.wait_variable(campo_minado.root.winfo_children()[0].iniciar)

#     # Verifique se o jogo foi iniciado com os parâmetros corretos
#     resultado = campo_minado.iniciar_jogo(8, 8, 10)
#     assert resultado == "Fácil", f"O nível selecionado deveria ser 'Fácil', mas foi '{resultado}'."