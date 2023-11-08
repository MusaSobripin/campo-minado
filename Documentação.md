## Requisitos gerados para a criação do jogo

*Requisitos para o Jogo:*

1. O jogo deve ser um jogo de Campo Minado ✅
2. O jogador deve ser capaz de selecionar um nível de dificuldade fácil no início do jogo. ✅
    -> Testar se é possível selecionar o nível de dificuldade fácil ✅
3. O jogador deve ser capaz de selecionar um nível de dificuldade intermediário no início do jogo. ✅
    -> Testar se é possível selecionar o nível de dificuldade intermediário ✅
4. O jogador deve ser capaz de selecionar um nível de dificuldade difícil no início do jogo. ✅
    -> Testar se é possível selecionar o nível de dificuldade fácil ✅
5. O jogo deve gerar um tabuleiro com base no nível de dificuldade selecionado. ✅
6. O tabuleiro deve ser composto por células retangulares que o jogador pode revelar. ✅
7. O tabuleiro deve ser preenchido com um número específico de bombas com base no nível de dificuldade. ✅
8. O jogador deve ser capaz de clicar nas células para revelar o conteúdo delas. ✅
9. Se o jogador clicar em uma célula com uma bomba, o jogo deve terminar com uma derrota.✅
10. As células reveladas devem mostrar o número de bombas adjacentes a elas.✅
11. Se uma célula não tiver bombas adjacentes, todas as células adjacentes a ela sem bombas adjacentes devem ser reveladas automaticamente.✅
12. O jogador deve ser capaz de marcar ou desmarcar uma célula com uma bandeira para indicar a presença de uma bomba.✅
13. O jogador só deve ser capaz de marcar uma célula como uma bandeira se não tiver sido revelada.✅
14. O jogador deve ser capaz de remover uma bandeira previamente colocada em uma célula.✅
15. O jogador deve ser capaz de reiniciar o jogo a qualquer momento. ✅
16. O jogo deve calcular o tempo que o jogador leva para concluir o jogo. ✅
17. O jogador deve ser capaz de vencer o jogo ao revelar todas as células sem bombas sem explodir nenhuma. ✅
18. O jogo deve mostrar uma mensagem de vitória quando o jogador vencer. ✅
19. O jogo deve mostrar uma mensagem de derrota quando o jogador perde.✅
20. O jogador deve ser capaz de iniciar um novo jogo após uma vitória ou derrota. ✅
21. O jogo deve permitir que o jogador saia do jogo e retorne ao menu principal a qualquer momento. ✅


*Requisitos de Interface do Usuário:*

22. O jogo deve ter uma interface gráfica amigável. ✅
23. Deve haver um menu principal na tela de jogo para retornar ao menu principal. ✅
24. Deve haver uma contagem de bombas marcadas na tela de jogo. 
25. Deve haver um cronômetro na tela de jogo para registrar o tempo de jogo. 
26. O tabuleiro do jogo deve ser visível e interativo. ✅
27. O jogo deve exibir células fechadas como um bloco sólido. ✅
28. As células reveladas devem mostrar o número de bombas adjacentes. ✅
29. O jogo deve usar bandeiras para indicar células com bombas marcadas pelo jogador. ✅
30. As células com bandeiras devem ser claramente identificáveis. ✅
31. O jogo deve ter mensagens de vitória e derrota visíveis na tela de jogo. ✅
32. O jogo deve ter uma tela de menu principal com opções para iniciar um novo jogo, acessar o histórico de resultados e sair do jogo. ✅ 
33. Deve haver opções de nível de dificuldade claramente visíveis no menu principal. ✅
34. O histórico de resultados deve ser apresentado de forma legível e organizada. ✅
35. O jogo deve ter um design agradável e fácil de usar. ✅
36. Deve haver um ícone ou logotipo representativo na interface. ✅
37. O jogo deve apresentar um tutorial explicando a forma correta de jogar ✅
38. O joog deve possuir um arquivo executável ✅
39. O jogo deve ter limite de bandeiras a serem inseridas de acordo com a quantidade de bombas existente no tabuleiro ✅
40. O jogo deve exibir um placar com a quantidade de bandeiras que restam sem ser marcadas ✅
41. O jogo deve exibir um placar com um cronômetro exibindo o tempo de jogo de cada partida ✅
42. O jogo deve ser testado e para evitar que haja bugs e que garantir seu pleno funcinamento ✅

## Técnicas utilizadas

### Testes de Unidade
```sh
Exemplos: 
test_plantar_bombas.py 
test_calcular_vizinhos.py
...
```

### Testes de Unidade
```sh
Exemplos: 
test_eventos_de_clique_facil.py
test_eventos_de_clique_intermediario.py
...
```

### Testes de Desempenho
```sh
Exemplos: 
test_desempenho_tabuleiro_pequeno_facil.py
test_desempenho_tabuleiro_pequeno_intermediario.py
...
```

### Testes de Interface de Usuário (UI)
```sh
Exemplos: 
test_criacao_do_menu.py
...
```

### Testes de Regrassão
```sh
Exemplos: 
...
```

## Tipos de Testes que foram realizados no jogo

### Testes de Bombas
#### Testes de Bombas: Esses testes verificam se as bombas são plantadas corretamente e se as contagens de bombas adjacentes são calculadas corretamente. 
*test_plantar_bombas*
*test_calcular_vizinhos*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_facil*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_intermediario*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_dificil*

### Testes de Casos extremos
#### Testes de Casos Extremos: São testes que exploram situações incomuns ou extremas, como tamanhos mínimos e máximos de tabuleiro, bem como coordenadas extremas.
*test_tamanho_minimo_do_tabuleiro*
*test_tamanho_maximo_do_tabuleiro*
*test_coordenadas_extremas_facil*
*test_coordenadas_extremas_intermediario*
*test_coordenadas_extremas_dificil*

### Testes de Clicks
#### Testes de Clicks: Verificam se os cliques nas células funcionam como esperado, incluindo casos de revelação de células vazias, cliques inválidos e cliques em bombas.
*test_revelar_celula_vazia_facil*
*test_revelar_celula_vazia_intermediario*
*test_revelar_celula_vazia_dificil*
*test_cliques_invalidos_facil*
*test_cliques_invalidos_intermediario*
*test_cliques_invalidos_dificil*
*test_clicar_com_bomba_facil*
*test_clicar_com_bomba_intermediario*
*test_clicar_com_bomba_dificil*

### Testes de Vizinhança
#### Testes de Vizinhança: Esses testes avaliam se as células adjacentes são identificadas corretamente, incluindo aquelas com ou sem bombas nas proximidades.
*test_celula_sem_vizinhos_facil*
*test_celula_sem_vizinhos_intermediario*
*test_celula_sem_vizinhos_dificil*
*test_celula_com_8_vizinhos_facil*
*test_celula_com_8_vizinhos_intermediario*
*test_celula_com_8_vizinhos_dificil*
*test_celula_na_borda_sem_vizinhos_facil*
*test_celula_na_borda_sem_vizinhos_intermediario*
*test_celula_na_borda_sem_vizinhos_dificil*
*test_celula_na_borda_com_3_vizinhos_facil*
*test_celula_na_borda_com_3_vizinhos_intermediario*
*test_celula_na_borda_com_3_vizinhos_dificil*
*test_celula_na_esquina_com_2_vizinhos_facil*
*test_celula_na_esquina_com_2_vizinhos_intermediario*
*test_celula_na_esquina_com_2_vizinhos_dificil*
*test_revelar_vizinhanca_com_celulas_contendo_zero_facil*
*test_revelar_vizinhanca_com_celulas_contendo_zero_intermediario*
*test_revelar_vizinhanca_com_celulas_contendo_zero_dificil*
*test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_facil*
*test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_intermediario*
*test_revelar_vizinhanca_com_celulas_valores_maiores_que_zero_dificil*
*test_revelar_vizinhanca_limite_do_tabuleiro_facil*
*test_revelar_vizinhanca_limite_do_tabuleiro_intermediario*
*test_revelar_vizinhanca_limite_do_tabuleiro_dificil*
*test_celula_sem_vizinhos_bomba*
*test_celula_sem_vizinhos_bomba_facil*
*test_celula_sem_vizinhos_bomba_intermediario*
*test_celula_sem_vizinhos_bomba_dificil*
*test_celula_com_vizinhos_bomba_em_todas_as_direcoes*
*test_celula_com_vizinhos_bomba_facil*
*test_celula_com_vizinhos_bomba_intermediario*
*test_celula_com_vizinhos_bomba_dificil*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_facil*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_intermediario*
*test_celula_com_vizinhos_bomba_em_algumas_direcoes_dificil*
*test_celula_na_borda_do_tabuleiro_facil*
*test_celula_na_borda_do_tabuleiro_intermediario*
*test_celula_na_borda_do_tabuleiro_dificil*
*test_celula_no_canto_do_tabuleiro_facil*
*test_celula_no_canto_do_tabuleiro_intermediario*
*test_celula_no_canto_do_tabuleiro_dificil*
*test_celula_fora_dos_limites_do_tabuleiro_facil*
*test_celula_fora_dos_limites_do_tabuleiro_intermediario*
*test_celula_fora_dos_limites_do_tabuleiro_dificil*
*test_celula_na_esquina_com_1_vizinhos_bomba_facil*
*test_celula_na_esquina_com_1_vizinhos_bomba_intermediario*
*test_celula_na_esquina_com_1_vizinhos_bomba_dificil*
*test_celula_na_esquina_com_2_vizinhos_bomba_facil*
*test_celula_na_esquina_com_2_vizinhos_bomba_intermediario*
*test_celula_na_esquina_com_2_vizinhos_bomba_dificil*
*test_celula_na_esquina_com_3_vizinhos_bomba_facil*
*test_celula_na_esquina_com_3_vizinhos_bomba_intermediario*
*test_celula_na_esquina_com_3_vizinhos_bomba_dificil*


### Testes de Menu
#### Testes de Menu: Verificam a criação e funcionalidade do menu principal do jogo.
*test_criacao_do_menu*

### Testes de Tabuleiro
#### Testes de Tabuleiro: Avaliam a criação e desempenho do tabuleiro em diferentes tamanhos e níveis de dificuldade.
*test_desempenho_tabuleiro_pequeno_facil*
*test_desempenho_tabuleiro_pequeno_intermediario*
*test_desempenho_tabuleiro_pequeno_dificil*
*test_desempenho_time_tabuleiro_pequeno*
*test_desempenho_tabuleiro_medio*
*test_desempenho_tabuleiro_grande*
*test_criacao_do_tabuleiro*
*test_eventos_de_clique_facil*
*test_eventos_de_clique_intermediario*
*test_eventos_de_clique_dificil*
*test_vinculacao_de_eventos*
*test_tabuleiro_vazio_facil*
*test_tabuleiro_vazio_intermediario*
*test_tabuleiro_vazio_dificil*
*test_tabuleiro_apenas_bombas_intermediario*
*test_tabuleiro_vizinho_de_bombas_facil*
*test_tabuleiro_vizinho_de_bombas_intermediario*
*test_tabuleiro_grande_facil*
*test_tabuleiro_grande_intermediario*
*test_tabuleiro_grande_dificil*
*test_dimensoes_nivel_facil*
*test_dimensoes_nivel_intermediario*
*test_dimensoes_nivel_dificil*

### Testes de Finalização da Partida
#### Testes de Finalização da Partida: Verificam se o jogo encerra corretamente quando necessário, considerando o tempo decorrido e a situação de vitória ou derrota.
*test_finalizar_partida_tempo_passado_facil*
*test_finalizar_partida_tempo_passado_intermediario*
*test_finalizar_partida_tempo_passado_dificil*
*test_finalizar_partida_tempo_passado_zero_facil*
*test_finalizar_partida_tempo_passado_zero_intermediario*
*test_finalizar_partida_tempo_passado_zero_dificil*
*test_finalizar_partida_tempo_passado_arredondado_facil*
*test_finalizar_partida_tempo_passado_arredondado_intermediario*
*test_finalizar_partida_tempo_passado_arredondado_dificil*

### Testes de Interação de Botões
#### Testes de Interação de Botões: Garantem que os botões do jogo funcionem corretamente e respondam aos eventos do usuário.
*test_interacao_de_botoes_facil*
*test_interacao_de_botoes_facil*
*test_interacao_de_botoes_facil*
*test_numero_de_botoes*
*test_ordem_dos_botoes*

### Testes de Marcação de Bandeiras
#### Testes de Marcação de Bandeiras: Verificam se o jogador pode marcar e desmarcar células com bandeiras de maneira apropriada.
*test_marcar_bandeira_em_celula_sem_bandeira_facil*
*test_marcar_bandeira_em_celula_sem_bandeira_intermadiario*
*test_marcar_bandeira_em_celula_sem_bandeira_dificil*
*test_desmarcar_bandeira_em_celula_marcada_facil*
*test_desmarcar_bandeira_em_celula_marcada_intermediario*
*test_desmarcar_bandeira_em_celula_marcada_dificil*
*test_marcar_bandeira_em_celula_com_bomba_facil*
*test_marcar_bandeira_em_celula_com_bomba_intermediario*
*test_marcar_bandeira_em_celula_com_bomba_dificil*

### Testes de Mensagens
#### Testes de Mensagens: Testam se as mensagens de vitória e derrota são exibidas corretamente, considerando diferentes cenários de jogo.
*test_encerramento_do_jogo_quando_nao*
*test_encerramento_do_jogo_quando_nao_facil*
*test_encerramento_do_jogo_quando_nao_intermediario*
*test_encerramento_do_jogo_quando_nao_dificil*
*test_reinicio_do_jogo_quando_sim_facil*
*test_reinicio_do_jogo_quando_sim_intermediario*
*test_reinicio_do_jogo_quando_sim_dificil*
*test_continuacao_do_jogo_quando_nao_facil*
*test_continuacao_do_jogo_quando_nao_intermediario*
*test_continuacao_do_jogo_quando_nao_dificil*

### Testes de Reiniciar o jogo
#### Testes de Reiniciar o jogo: Verificam se o jogo pode ser reiniciado após uma vitória ou derrota, garantindo que os valores padrão sejam restaurados.
*test_reiniciar_jogo_jogo_encerrado_facil*
*test_reiniciar_jogo_jogo_encerrado_intermediario*
*test_reiniciar_jogo_jogo_encerrado_dificil*
*test_reiniciar_jogo_valores_padrao_facil*
*test_reiniciar_jogo_valores_padrao_intermediario*
*test_reiniciar_jogo_valores_padrao_dificil*

### Testes de de Situação do Jogo
#### Testes de Situação do Jogo: Avaliam o comportamento do jogo em diferentes estados, como o jogo iniciado, encerrado, etc.
*test_jogo_iniciado_facil*
*test_jogo_iniciado_intermediario*
*test_jogo_iniciado_dificil*
*test_jogo_encerrado*

### Testes de Verificar Vitória
#### Testes de Verificar Vitória: Esses testes se concentram em verificar se as condições de vitória são detectadas corretamente durante o jogo.
*test_verificar_vitoria_jogo_em_andamento_facil*
*test_verificar_vitoria_jogo_em_andamento_intermediario*
*test_verificar_vitoria_jogo_em_andamento_dificil*
*test_verificar_vitoria_vitoria_facil*
*test_verificar_vitoria_vitoria_intermediario*
*test_verificar_vitoria_vitoria_dificil*
*test_verificar_vitoria_derrota_facil*
*test_verificar_vitoria_derrota_intermediario*
*test_verificar_vitoria_derrota_dificil*