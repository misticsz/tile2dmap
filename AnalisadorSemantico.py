from ANTLR.tileVisitor import *
from ANTLR.tileParser import *

class AnalisadorSemantico(tileVisitor):

    def get_warnings(self):
        return self.warnings[:-1]


    def visitMapa(self, ctx: tileParser.MapaContext):
        print(ctx.size().getText())
        if ctx.size() is None:
            self.get_erro_parametro_nao_permitido(ctx.start,'cor')
        return
