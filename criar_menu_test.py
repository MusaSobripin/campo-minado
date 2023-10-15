import tkinter
import pytest
from tkinter import Tk
from cnpjto import CampoMinado 

@pytest.fixture
def campo_minado():
    root = Tk()
    root.withdraw()
    game = CampoMinado(root)
    yield game
    root.quit()
    
def test_criacao_do_menu(campo_minado):
    label, buttons = campo_minado.criar_menu_niveis()

    # Verifique se os widgets esperados foram criados
    assert isinstance(label, tkinter.Label)
    assert len(buttons) == 3  # Suponha que haja três botões

    # Verifica se o rótulo e os botões estão organizados corretamente no frame
    assert label.master.winfo_exists()
    for button in buttons:
        assert button.master.winfo_exists()

    campo_minado.root.destroy()
    