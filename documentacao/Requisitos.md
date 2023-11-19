## Requisitos gerados para a criação do jogo

*Requisitos para o Jogo:*

1. O jogo deve ser um jogo de Campo Minado ✅
    + Testar nível facil 
    + Testar nível intermediário 
    + Testar nível difícil

2. O jogador deve ser capaz de selecionar um nível de dificuldade fácil no início do jogo. ✅
    + Testar se é possível selecionar o nível de dificuldade fácil 
    + Testar se o tabuleiro é do nível fácil

3. O jogador deve ser capaz de selecionar um nível de dificuldade intermediário no início do jogo. 
    + Testar se é possível selecionar o nível de dificuldade intermediário 
    + Testar se o tabuleiro é do nível intermediário

4. O jogador deve ser capaz de selecionar um nível de dificuldade difícil no início do jogo. ✅
    + Testar se é possível selecionar o nível de dificuldade fácil ✅
    + Testar se o tabuleiro é do nível dificil

5. O jogo deve gerar um tabuleiro com base no nível de dificuldade selecionado. ✅
    + Iniciar jogo em cada nível
    + Testar se o tabuleiro é do tamanho apropriado

6. O tabuleiro deve ser composto por células retangulares que o jogador pode revelar. ✅
    + Testar se as células são clicaveis

7. O tabuleiro deve ser preenchido com um número específico de bombas com base no nível de dificuldade. ✅
    + Testar se o tabuleiro possui o nível de bombas adequado

8. O jogador deve ser capaz de clicar nas células para revelar o conteúdo delas. ✅
    + Testar se as células são reveladas corretamente

9. Se o jogador clicar em uma célula com uma bomba, o jogo deve terminar com uma derrota.✅
    + Testar se o jogo é encerrado quando clica em bomba 

10. As células reveladas devem mostrar o número de bombas adjacentes a elas.✅
    + Testar exibem a quantidade de bombas

11. Se uma célula não tiver bombas adjacentes, todas as células adjacentes a ela sem bombas adjacentes devem ser reveladas automaticamente.✅
    + Verificar se a célula sem bomba vizinha é revelad
    + Verificar se as células vizinhas sem bomba são reveladas

12. O jogador deve ser capaz de marcar ou desmarcar uma célula com uma bandeira para indicar a presença de uma bomba.✅
    + Tentar marcar uma célula com uma bandeira.
    + Tentar desmarcar uma célula marcada com uma bandeira.

13. O jogador só deve ser capaz de marcar uma célula como uma bandeira se não tiver sido revelada.✅
    + Tentar marcar uma célula já revelada.
    + Tentar marcar uma célula não revelada.

14. O jogador deve ser capaz de remover uma bandeira previamente colocada em uma célula.✅
    + Tentar remover uma bandeira de uma célula marcada.
    + Tentar remover uma bandeira de uma célula não marcada.

15. O jogador deve ser capaz de reiniciar o jogo a qualquer momento. ✅
    + Reiniciar o jogo durante a jogada e verificar se o tabuleiro é redefinido

16. O jogo deve calcular o tempo que o jogador leva para concluir o jogo. ✅
    + Iniciar o jogo e verificar se o tempo é contabilizado.
    + Reiniciar o jogo e verificar se o tempo é reiniciado.

17. O jogador deve ser capaz de vencer o jogo ao revelar todas as células sem bombas sem explodir nenhuma. ✅
    + Jogar até revelar todas as células sem bombas
    + Garantir que o jogo seja vencido.

18. O jogo deve mostrar uma mensagem de vitória quando o jogador vencer. ✅
    + Vencer o jogo e verificar se uma mensagem de vitória é exibida.

19. O jogo deve mostrar uma mensagem de derrota quando o jogador perde.✅
    + Perder o jogo clicando em uma célula com bomba e verificar se uma mensagem de derrota é exibida.

20. O jogador deve ser capaz de iniciar um novo jogo após uma vitória ou derrota. ✅
    + Vencer o jogo e iniciar um novo jogo.
    + Perder o jogo e iniciar um novo jogo.

21. O jogo deve permitir que o jogador saia do jogo e retorne ao menu principal a qualquer momento. ✅
    + Sair do jogo durante a jogada e verificar se é possível retornar ao menu principal.


*Requisitos de Interface do Usuário:*

22. O jogo deve ter uma interface gráfica amigável. ✅
    + Observar a interface do jogo e avaliar a facilidade de uso e a estética.

23. Deve haver um menu principal na tela de jogo para retornar ao menu principal. ✅
    + Durante o jogo, verificar se é possível acessar o menu principal.

24. Deve haver uma contagem de bombas marcadas na tela de jogo. 
    + Marcar algumas células com bandeira e verificar se a contagem é atualizada corretamente.

25. Deve haver um cronômetro na tela de jogo para registrar o tempo de jogo. 
    + Iniciar o jogo e verificar se o cronômetro começa a registrar o tempo.

26. O tabuleiro do jogo deve ser visível e interativo. ✅
    + Iniciar o jogo e verificar se o tabuleiro é visível.
    + Tentar interagir com o tabuleiro para garantir que seja interativo.

27. O jogo deve exibir células fechadas como um bloco sólido. ✅
    + Verificar se as células fechadas são claramente identificadas na interface.

28. As células reveladas devem mostrar o número de bombas adjacentes. ✅
    + Revelar células e verificar se o número de bombas adjacentes é exibido corretamente.

29. O jogo deve usar bandeiras para indicar células com bombas marcadas pelo jogador. ✅
    + Marcar células com bandeira e verificar se são identificadas corretamente.

30. As células com bandeiras devem ser claramente identificáveis. ✅
    + Marcar células com bandeira e verificar se as bandeiras são visíveis e distintas.

31. O jogo deve ter mensagens de vitória e derrota visíveis na tela de jogo. ✅
    + Vencer o jogo e verificar se a mensagem de vitória é exibida.
    + Perder o jogo e verificar se a mensagem de derrota é exibida.

32. O jogo deve ter uma tela de menu principal com opções para iniciar um novo jogo, acessar o histórico de resultados e sair do jogo. ✅ 
    + Acessar o menu principal durante o jogo e verificar as opções disponíveis.

33. Deve haver opções de nível de dificuldade claramente visíveis no menu principal. ✅
    + Acessar o menu principal e verificar se as opções de dificuldade são visíveis.

34. O histórico de resultados deve ser apresentado de forma legível e organizada. ✅
    + Acessar o histórico de resultados e verificar a apresentação e organização das informações.

35. O jogo deve ter um design agradável e fácil de usar. ✅
    + Avaliar o design global do jogo em termos de estética e usabilidade.

36. Deve haver um ícone ou logotipo representativo na interface. ✅
    + Observar a presença e a representação do ícone ou logotipo na interface.

37. O jogo deve apresentar um tutorial explicando a forma correta de jogar ✅
    + Acessar o tutorial e verificar se fornece informações claras sobre como jogar.

38. O joog deve possuir um arquivo executável ✅
    + Executar o arquivo executável e verificar se o jogo inicia corretamente.

39. O jogo deve ter limite de bandeiras a serem inseridas de acordo com a quantidade de bombas existente no tabuleiro ✅
    + Tentar adicionar mais bandeiras do que o permitido e verificar se há restrições.

40. O jogo deve exibir um placar com a quantidade de bandeiras que restam sem ser marcadas ✅
    + Verificar se o placar de bandeiras é exibido corretamente durante o jogo.

41. O jogo deve exibir um placar com um cronômetro exibindo o tempo de jogo de cada partida ✅
    + Verificar se o placar com o cronômetro é exibido corretamente durante o jogo.

42. O jogo deve ser testado e para evitar que haja bugs e que garantir seu pleno funcinamento ✅
    + Realizar testes abrangentes em diferentes cenários para identificar e corrigir bugs.

- [Voltar ao início](#apresentando-o-jogo)