import antlr4
import os
import sys
import argparse
from ANTLR.tileLexer import *
from ANTLR.tileParser import *
from ErrosSintaticosErrorListener import ErrosSintaticosErrorListener

DIRETORIO_PROJETO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SINTATICO = 'lexico-sintatico/'


TESTE = SINTATICO

CAMINHO_ARQUIVOS_ENTRADA = '/tile2dmap/casos_de_teste/entrada/'



def casos_de_teste_sintatico():
    print('----------------------------------------------')
    print('CASOS DE TESTE DO ANALISADOR LÉXICO/SINTÁTICO ')
    print('----------------------------------------------')
    for i in range(0, 3):
        with open(DIRETORIO_PROJETO + CAMINHO_ARQUIVOS_ENTRADA + SINTATICO + 'ct_sintatico_' + str(i) + '.txt',
                  encoding='utf-8') as caso_de_teste:
            programa = caso_de_teste.read()

            programa_input = antlr4.InputStream(programa)



            lexer = tileLexer(input=programa_input)
            lexer.removeErrorListeners()
            tokens = antlr4.CommonTokenStream(lexer=lexer)

            parser = tileParser(tokens)

            parser.removeErrorListeners()
            erros_sintaticos = ErrosSintaticosErrorListener()
            parser.addErrorListener(erros_sintaticos)
            try:
                parser.mapa()
                print('[CT' + str(i) + '_SINTATICO] compilação finalizada.')
            except Exception as e:
                print('[CT' + str(i) + '_SINTATICO] ' + str(e), file=sys.stderr)
                pass



def main():
    casos_de_teste_sintatico()

if __name__ == '__main__':
    main()
