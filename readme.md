# Tile 2D Map - Universidade Federal de Sao Carlos

Uma linguagem gerada para criação de mapas através da utilização de tiles.

## Introdução

### Prerequisites

Python 3 - https://www.python.org/downloads/

Pip - Geralmente vem junto a instalação do Python.

Antlr4 for Python 3 - ```pip3 install antlr4-python3-runtime ```

### Instalação

Enquanto estiver na pasta do projeto


```
Pyhton3 Main.py
```

## Casos
0 - Apenas SINTATICO
1 - Apenas SEMANTICO
2 - Gerador de Codigo

##Imagens

Você pode adqurir varios tiles atraves de spreadsheets , alguns abaixo para conseguir algumas de graça :)


https://opengameart.org/content/2d-complete-characters
http://kenney.nl/
https://crateboy.itch.io/crateboy-2007-2014

Apos pegar o sprite sheet so dividilos do tamanho exato no site


### Exemplos e como utilizar

```
map(size:25) { // MAPA AGUA GELO
  import {

   water{
            path: "mario/sprite_125.png"
            nivel : 1
        }

   ice {
        path: "mario/sprite_318.png"
        nivel : 2
   }

    trap{
        path: "mario/sprite_087.png"
        nivel : 2
    }

    tunel{
        path: "mario/sprite_809.png"
        nivel : 2
    }
  }

  commands{
    loop coluna 2 0 ate 2 ice
    loop linha 2 2 ate 4 ice
    loop coluna 4 2 ate 4 ice
    loop linha 4 4 ate 11 ice
    loop coluna 11 4 ate 14 ice
    loop linha 11 8 ate 10 ice
    loop linha 12 12 ate 14 ice
    loop linha 16 12 ate 19 ice
    add tunel (11 8)
    add tunel (16 14)
    add trap (15 11)
    add trap (11 14)
    add trap (13 14)
    loop coluna 15 11 ate 14 trap
  }
}
```
![Map](https://imgur.com/muHCT4S)


##Commands

#Add
  add `tile` ( n1 n2 )  com n1 e n2 sendo posicao na matriz
#Remove
  remove `tile` ( n1 n2 )  com n1 e n2 sendo posicao na matriz
#Especial
  `acao` `tile` ( n1 n2 )  com n1 e n2 sendo posicao na matriz
#Loop
  loop `linha` ou `coluna` qual n1 ate n2   n1 e n2 sendo a variacao

