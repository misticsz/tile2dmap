from ANTLR.tileVisitor import *
from ANTLR.tileParser import *


class Tiles:
    def __init__(self, path, name, Acao):
        self.path = path
        self.name = name
        self.acao = Acao

    def set_acao(self,Acao):
        self.acao = Acao


class Acao:
    def __init__(self, path, name):
        self.path = path
        self.name = name


class AnalisadorSemantico(tileVisitor):

    #Variaveis Globais
    size = 0
    imageCounter = 1
    acaoCounter = 0
    acao = []
    limpa = []
    acaoTemp = []
    tile = []
    acao.append((Acao("/default","default")))
    tile.append((Tiles("/default","default",acao)))

    ## - Mensagens de Erro - ##

    def get_linha_do_erro(self, dados_do_erro):
        return 'Erro semântico na linha ' + str(dados_do_erro).split(',')[3].split(':')[0] + ': '

    def get_linha_do_warning(self, dados_do_erro):
        return str(dados_do_erro).split(',')[3].split(':')[0]

    def get_regra_do_erro(self, dados_do_erro):
        return ' no comando ' + str(dados_do_erro).split(',')[1].split('=')[1] + '.'


    def get_erro_variavel_ja_declarada(self,dados,variavel):
        erro = self.get_linha_do_erro(dados) + 'a variavel " ' + variavel + ' " ja foi declarada' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_tamanho(self,dados):
        erro = self.get_linha_do_erro(dados) + 'posicao invalida ' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_acao_ja_declarada(self,dados,variavel):
        erro = self.get_linha_do_erro(dados) + 'a acao " ' + variavel + ' " ja foi declarada' + \
               self.get_regra_do_erro(dados)
        raise Exception(erro)

    def get_erro_nao_declarada(self,dados,variavel):
        erro = self.get_linha_do_erro(dados) + 'a variavel" ' + variavel + ' " nao existe'
        raise Exception(erro)



    # Funcao para verficar se variavel esta na tabela #
    def checkTable(self,name,tile,imageCounter):
        for i in range(0, imageCounter):
            if(tile[i].name==name):
                return 0
        return 1


    # Funcao para verficar se acao esta na tabela #
    def checkTableAction(self,name,action):
        for i in action:
            if i.name == name:
                return 0
        return 1


    def visitMapa(self, ctx: tileParser.MapaContext):
        self.size = str(ctx.size().NUM_INT());
        if ctx.tile() is not None:
            self.visitTile(ctx.tile())
        if ctx.commands() is not None:
            self.visitCommands(ctx.commands())


#        if ctx.commands() is not None:
#            return visitCommands(ctx.commands())


    def visitTile(self,ctx: tileParser.TileContext):
        if ctx is not None:
            path = str(ctx.path().CADEIA())
            name = str(ctx.ID())
            # Verficao feita facilmente sendo que criamos um objeto para tiles e dentro de tiles possuimos varias acoes #
            if(self.checkTable(name,self.tile,self.imageCounter)):
                if ctx.acao() is not None:
                    self.acaoCounter = 1
                    self.acaoTemp = []
                    self.visitAcao(ctx.acao())
                    self.tile.append((Tiles(path,name, self.acaoTemp)))
                    self.imageCounter+=1
            else:
                self.get_erro_variavel_ja_declarada(ctx.start, name)

        return self.visitRecur_tiles(ctx.recur_tiles())


    def visitAcao(self,ctx: tileParser.AcaoContext):
        if ctx is not None:
            path = str(ctx.path().CADEIA())
            name = str(ctx.ID())
            if(self.checkTableAction(name,self.acaoTemp)):
                self.acaoCounter+=1
                self.acaoTemp.append((Acao(path,name)))
            else:
                self.get_erro_acao_ja_declarada(ctx.start, name)

        self.visitRecur_acao(ctx.recur_acao())

        return path

    def visitCommands(self, ctx: tileParser.CommandsContext):
        if ctx is not None:
            if ctx.add() is not None:
                name = str(ctx.add().ID())
                if(int(ctx.add().n1.text)>int(self.size) or int(ctx.add().n2.text)>int(self.size)):
                    self.get_erro_tamanho(ctx.start)
                if(self.checkTable(name,self.tile,self.imageCounter)==1):
                    self.get_erro_nao_declarada(ctx.start,name)

            if ctx.remove() is not None:
                name = str(ctx.remove().ID())
                if(int(ctx.remove().n1.text)>int(self.size) or int(ctx.remove().n2.text)>int(self.size)):
                    self.get_erro_tamanho(ctx.start)
                if(self.checkTable(name,self.tile,self.imageCounter)==1):
                    self.get_erro_nao_declarada(ctx.start,name)

            self.visitRecur_commands(ctx.recur_commands())

            return name


    def visitRecur_tiles(self, ctx: tileParser.Recur_tilesContext):
        return "\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''

    def visitRecur_acao(self, ctx: tileParser.Recur_acaoContext):
        return "\n"+self.visitAcao(ctx.acao()) if ctx.acao() is not None else ''

    def visitRecur_commands(self, ctx: tileParser.Recur_commandsContext):
        return "\n"+self.visitCommands(ctx.commands()) if ctx.commands() is not None else ''
