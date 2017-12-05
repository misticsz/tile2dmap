from ANTLR.tileVisitor import *
from ANTLR.tileParser import *

class AnalisadorSemantico(tileVisitor):

    def get_warnings(self):
        return self.warnings[:-1]


    def visitMapa(self, ctx: tileParser.MapaContext):
        print(ctx.size().INTEGER_NUMBER())
