# Jogo de Xadrez
 *_Projeto de Engenharia de Software - UFF_*

 Professor: Leonardo Murta.

 Integrantes : 
 
               João Pedro Fontinele,

               Valter Neto,
               
               Fillipi Cunha
               
               Rodrigo Ribeiro.


### Tecnologia

Este é um simples jogo de xadrez em que você pode desafiar o computador. O computador utiliza o algoritmo [Minimax](https://pt.wikipedia.org/wiki/Minimax) para selecionar suas jogadas, otimizado para tomar decisões melhores com o uso do algoritmo de otimização [Alpha-Beta-Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

### Tutorial

Para jogar, selecione "Jogar" no menu principal e, em seguida, selecionar uma peça do tabuleiro com o mouse, serão exibidas as opções de movimento disponíveis para a peça selecionada. Ao escolher o quadrado para o qual deseja mover a peça, o jogo irá atualizar as posições e a vez será passada para o computador. O jogo segue as regras do xadrez clássico.


### Como iniciar o Teste de Unidade

O teste de unidade consiste em verificar as entradas e saídas do jogo. Todos os testes devem retornar "ok". Para realizar os testes de unidade, foi utilizada a biblioteca unittest.

```bash
python3 -m unittest -v unitTestChess.Test
#ou
python3 -m unitTestChess -v
```
