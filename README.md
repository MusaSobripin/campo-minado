# CAMPO MINADO
Trabalho prático individual de Tópicos Especiais II pedido pelo professor Alcemir Santos - 2023.1

## DESCRIÇÃO
Você trabalha numa empresa que desenvolve jogos simples para permitir que os usuários passem o seu tempo livre jogando. Sua equipe acaba de fazer um brainstorming e decidir quais e quem desenvolveria os próximos jogos. Você ficou responsável por desenvolver um jogo de Campo Minado. A equipe já desenhou o protótipo de baixa fidelidade, que é ilustrado ao lado.

## REQUISITOS

Asregras do jogo são simples: O jogador deve marcar com uma bandeira todos as zonas que ele imaginar conter uma bomba. O jogador só tem três ações possíveis: (i) colocar uma bandeira em uma zona indicando que a mesma contém uma bomba, (ii) remover uma bandeira previamente colocada ou (iii) e descobrir uma zona sem bandeira. Não é possível descobrir uma zona com 
bandeira, é necessário remover uma bandeira antes de descobri-la. Não é possível cobrir uma zona depois de descobri-la. Todas as zonas iniciam cobertas e sem bandeira. Cada zona pode ser área limpa ou conter uma bomba. As zonas limpas que fazem fronteira com zonas com bomba, indicam quantas bombas aparecem adjacentes a ela. Cada zona pode ter de zero (0) a oito (8) zonas que contém bomba adjacentes a ela. A quantidade de bombas adjacentes a uma zona é revelada ao descobri-la. O jogador vence se descobrir todas as zonas contendo bomba, sem 
explodir nenhuma. Uma bomba explode se o jogador descobrir a zona que ela se encontra. A pontuação do jogo é dada pelo tempo levado para descobrir todas as bombas em segundos. O 
número de bombas é fixo a cada partida nível jogado. Considere três graus de dificuldade, dados pelas dimensões do tabuleiro e a densidade de bombas espalhadas no campo: fácil (8x8 – 10 bombas); intermediário (10x16 – 30 bombas); e difícil (24x24 – 100 bombas). Mantenha uma histórico de resultados para consulta.

Os casos de requisitos não especificados devem ser coletados com o professor da disciplina.
