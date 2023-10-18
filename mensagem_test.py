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
    
def test_encerramento_do_jogo_quando_nao(campo_minado):
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")

def test_encerramento_do_jogo_quando_sim(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você ganhou!")

# def test_reinicio_do_jogo_quando_sim(campo_minado):
#     with pytest.raises(SystemExit):
#         campo_minado.mostrar_mensagem("Você perdeu!")
#     assert campo_minado.nivel == (8, 8, 10)

# def test_continuacao_do_jogo_quando_nao(campo_minado):
#     with pytest.raises(SystemExit):
#         campo_minado.mostrar_mensagem("Você perdeu!")
#     assert campo_minado.nivel is None
