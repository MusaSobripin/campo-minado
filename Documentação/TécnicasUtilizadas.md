## Técnicas de testes utilizadas
```sh
>> Teste de Caixa-Preta
>> Teste Caixa-Branca (ou Testes Estruturais)
>> Testes de Unidade
>> Testes de Desempenho
>> Testes de Regressão
>> Testes de Stress
>> Testes de Classes de Equivalência
>> Testes de Aceitação
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

### Teste de Unidade

Descrição: *Centrados em testar unidades individuais do código.*
```sh
Exemplos: 
test_eventos_de_clique_facil.py
test_eventos_de_clique_intermediario.py
...
```

### Teste de Desempenho

Descrição: *Avaliam o desempenho do sistema em diferentes condições*
```sh
Exemplos: 
test_desempenho_tabuleiro_pequeno_facil.py
test_desempenho_tabuleiro_pequeno_intermediario.py
...
```

### Teste de Regressão

Descrição: *Garantem que novas alterações não quebrem funcionalidades existentes.*
```sh
Exemplos: 
test_reiniciar_jogo_valores_padrao_facil
test_encerramento_do_jogo_quando_nao
...
```

### Teste de Stress

Descrição: *Avaliam o comportamento do sistema sob condições extremas ou carga pesada.*
```sh
Exemplos: 
test_desempenho_tabuleiro_grande_facil
test_desempenho_time_tabuleiro_pequeno
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

### Teste de Aceitação

Descrição: *Garantem que o sistema atenda aos critérios de aceitação do cliente.*
```sh
Exemplos: 
test_verificar_vitoria_vitoria_dificil
test_encerramento_do_jogo_quando_nao_intermediario
...
```
