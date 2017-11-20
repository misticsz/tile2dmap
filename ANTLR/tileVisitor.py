# Generated from tile.g4 by ANTLR 4.7
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .tileParser import tileParser
else:
    from tileParser import tileParser

# This class defines a complete generic visitor for a parse tree produced by tileParser.

class tileVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by tileParser#mapa.
    def visitMapa(self, ctx:tileParser.MapaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#commands.
    def visitCommands(self, ctx:tileParser.CommandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#recur_commands.
    def visitRecur_commands(self, ctx:tileParser.Recur_commandsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#loop.
    def visitLoop(self, ctx:tileParser.LoopContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#add.
    def visitAdd(self, ctx:tileParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#remove.
    def visitRemove(self, ctx:tileParser.RemoveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#especial.
    def visitEspecial(self, ctx:tileParser.EspecialContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#tile.
    def visitTile(self, ctx:tileParser.TileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#acao.
    def visitAcao(self, ctx:tileParser.AcaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#recur_acao.
    def visitRecur_acao(self, ctx:tileParser.Recur_acaoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#recur_tiles.
    def visitRecur_tiles(self, ctx:tileParser.Recur_tilesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#size.
    def visitSize(self, ctx:tileParser.SizeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#nivel.
    def visitNivel(self, ctx:tileParser.NivelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by tileParser#path.
    def visitPath(self, ctx:tileParser.PathContext):
        return self.visitChildren(ctx)



del tileParser