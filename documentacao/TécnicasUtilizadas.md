## Técnicas de testes utilizadas
```sh
>> Teste de Caixa-Preta
>> Teste Caixa-Branca (ou Testes Estruturais)
>> Testes de Classes de Equivalência
```

### Teste de Caixa-Preta

Descrição: *Técnicas que se concentram nos requisitos externos sem conhecimento detalhado da implementação interna.*
```sh
Exemplos: 
test_revelar_celula_vazia_facil.py 
test_verificar_vitoria_vitoria_dificil.py
...
```

### Teste Caixa-Branca (ou Testes Estruturais)

Descrição: *Técnicas que exploram a lógica interna do sistema*
```sh
Exemplos: 
test_plantar_bombas.py
test_calcular_vizinhos.py
...
```


### Teste de Classes de Equivalência

Descrição: *Agrupam entradas em classes e testam uma representante de cada classe.*
```sh
Exemplos: 
test_tamanho_minimo_do_tabuleiro
test_tabuleiro_vazio_dificil
...
```

- [Voltar ao início](#apresentando-o-jogo)