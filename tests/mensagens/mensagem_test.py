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

def test_encerramento_do_jogo_quando_nao_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")

def test_encerramento_do_jogo_quando_nao_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")

def test_encerramento_do_jogo_quando_nao_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")

def test_reinicio_do_jogo_quando_sim_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    campo_minado.mostrar_mensagem("Você perdeu!")
    
    if campo_minado.nivel is not None:     # Verifica se self.nivel não é None antes de chamar iniciar_jogo
        campo_minado.iniciar_jogo(*campo_minado.nivel)

    assert campo_minado.nivel == (8, 8, 10)

def test_reinicio_do_jogo_quando_sim_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    campo_minado.mostrar_mensagem("Você perdeu!")
    
    if campo_minado.nivel is not None:     # Verifica se self.nivel não é None antes de chamar iniciar_jogo
        campo_minado.iniciar_jogo(*campo_minado.nivel)

    assert campo_minado.nivel == (10, 16, 30)

def test_reinicio_do_jogo_quando_sim_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    campo_minado.mostrar_mensagem("Você perdeu!")
    
    if campo_minado.nivel is not None:     # Verifica se self.nivel não é None antes de chamar iniciar_jogo
        campo_minado.iniciar_jogo(*campo_minado.nivel)

    assert campo_minado.nivel == (24, 24, 100)

def test_continuacao_do_jogo_quando_nao_facil(campo_minado):
    campo_minado.iniciar_jogo(8, 8, 10)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")
    assert campo_minado.nivel == (8, 8, 10)

def test_continuacao_do_jogo_quando_nao_intermediario(campo_minado):
    campo_minado.iniciar_jogo(10, 16, 30)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")
    assert campo_minado.nivel == (10, 16, 30)
    
def test_continuacao_do_jogo_quando_nao_dificil(campo_minado):
    campo_minado.iniciar_jogo(24, 24, 100)
    with pytest.raises(SystemExit):
        campo_minado.mostrar_mensagem("Você perdeu!")
    assert campo_minado.nivel == (24, 24, 100)