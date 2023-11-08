# CAMPO MINADO

## Tópicos

- [Apresentando o jogo](#apresentando-o-jogo)
- [Como rodar o projeto?](#como-rodar-o-projeto)
- [Como consigo executar  os testes?](#como-executar-os-testes)
- [Documentação](./Documentação.md)

## Apresentando o jogo

### Menu do Jogo
![Tela do jogo no modo fácil.](./img/menu.png)

### Tutorial
![Tela do jogo no tutorial.](./img/tutorial.png)

### Jogo fácil

![Tela do jogo no modo fácil.](./img/facil.png)

### Jogo intermediário

![Tela do jogo no modo Intermediário.](./img/intermediario.png)

### Jogo Difícil
![Tela do jogo no modo difícil.](./img/dificil.png)

</p>

## Como rodar o Projeto?

### Entre na raiz do projeto 

```sh
cd campo-minado
```

### Instale todas as dependências

```sh
pip3 install -r dependencias.txt
```

### Execute o jogo já compilado

```sh
py cminado.py
```
ou
```sh
./dist/cminado.exe
```

## Como executar os testes?

### Dentro do diretório do projeto (caminho/campo-minado) execute

```sh
py -m pytest [nome_test.py]
```

### Testes no jogo
![Tela do jogo com os testes.](./img/testes.png)