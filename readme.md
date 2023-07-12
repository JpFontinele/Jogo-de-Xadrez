# Jogo de Xadrez
 ## *_Projeto de Engenharia de Software - UFF_*

 #### Professor: Leonardo Murta.

 ##### Integrantes : 
 
               João Pedro Fontinele,

               Valter Neto,
               
               Fillipi Cunha
               
               Rodrigo Ribeiro.


### Tecnologia e Algorítimos

Este é um jogo de xadrez simples, onde é possível desafiar o computador. O computador utiliza o algoritmo [Minimax](https://pt.wikipedia.org/wiki/Minimax) para selecionar suas jogadas, otimizado a tomada de decisões por meio do uso do algoritmo de otimização [Alpha-Beta-Pruning](https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning).

### Tutorial

A fim de rodar os arquivos .py é necessário ter o módulo pygame instalado. Para instalar o módulo (Linux) rode os comandos:

Instalação via PIP:
```
pip install pygame

#ou

pip3 install pygame
```

Instalação via APT:
```
sudo apt-get install idle pygame

#ou

sudo apt install python3-pygame
```

Para jogar, selecione "Jogar" no menu principal e, em seguida, selecione uma peça do tabuleiro com o mouse. Serão exibidas as opções de movimento disponíveis para a peça selecionada. Ao escolher o quadrado para o qual deseja mover a peça, o jogo irá atualizar as posições e a vez será passada para o computador. O jogo segue as regras do xadrez clássico.


### Como iniciar o Teste de Unidade

O teste de unidade consiste em verificar as entradas e saídas do jogo. Todos os testes devem retornar "ok". Para realizar os testes de unidade, foi utilizada a biblioteca unittest.

```bash
python3 -m unittest -v unitTestChess.Test
#ou
python3 -m unitTestChess -v
```

Notas:

* Caso seja necessário descompilar os arquivos .pyc, será necessária a utilização de um descompilador. Para instalar o Uncompyle6 (Linux) rode o comando:
```
sudo pip install uncompyle6

#ou

sudo pip3 install uncompyle6
```

### Estrutura

O jogo apresenta uma estrutura de pastas e arquivos simples.

##### Arquivos .py
Os códigos principais utilizados para a execução do jogo são os arquivos.py. No ``root`` da pasta é possível encontrar os arquivos "menu.py" e "jogo.py". Ambos, respectivamente, responsáveis pelo display do menu principal do jogo (ou "launcher") e do jogo em si. Ambos usam os arquivos da pasta "assets" para a construção da interface, juntamente com "invocação" de outros arquivos .py, que podem ser encontrados na pasta "modules".
<br />
Já dentro da pasta "modules" é possível encotrar os arquivos "board.py", "oponent.py" e "pieces.py", os quais são reponsáveis por, respectivamente, ditar o comportamento do tabuleiro, do oponente (no caso o computador) e das peças, individualmente, sustentando a execução do arquivo "jogo.py".
<br />
O arquivo "unit.TestChess.py", encontrado no ``root`` do jogo, é o arquivo utilizado para a realização do Teste de Unidade.

###### Pasta Assets
A pasta "assets" contém as imagens de referência para a execução do jogo, incluindo arquivos .png das peças, do tabuleiro e do menu principal.

##### Arquivo License
O arquivo License é aquele que contém as permissões de uso e distribuição do software em questão. É também o que carrega o copyright e os créditos de autoria do software.