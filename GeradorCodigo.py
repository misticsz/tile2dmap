from ANTLR.tileVisitor import *
from ANTLR.tileParser import *

class Tile():
    nome = ''
    acao = []

class GeradorCodigo(tileVisitor):

    #Array que armazena as imagens

    imageArray = []
    imageCounter = 0
    tileCounter = 0
    acaoCounter = 1

    final = """<!DOCTYPE html><html><head><script type="text/javascript">var ctx = null;size = {size}
    var i = 0;
    var gameMap = new Array();

    for(i=0;i<={size}*{size};i++){
        gameMap[i] = 0;
    }
    /*Tile Loading */
    var image = new Array();
    var tiles = new Array();

    {tiles}

    {images}

    var currentSecond = 0, frameCount = 0, framesLastSecond = 0;
    window.onload = function()
    {
    	ctx = document.getElementById('game').getContext("2d");
    	requestAnimationFrame(drawGame);
    	ctx.font = "bold 10pt sans-serif";
    };


    """


    def visitMapa(self,ctx: tileParser.MapaContext):
        size = str(ctx.size().INTEGER_NUMBER())
        self.final = self.final.replace('{size}',size)
        self.final = self.final.replace('{tiles}',str(self.visitTile(ctx.tile())))

    def visitTile(self,ctx: tileParser.TileContext):
        path = str(ctx.path().CADEIA())
        name = str(ctx.ID())
        tile = "tile["+str(self.imageCounter)+"] = { \n path:"+path+", name:'"+name+"', action :{"+self.visitAcao(ctx.acao(),self.imageCounter) + "}};" + "\nimage["+str(self.imageCounter)+"].src = tile["+str(self.imageCounter)+"].path;" + self.visitRecur_tiles(ctx.recur_tiles())

        return tile;

    def visitAcao(self,ctx: tileParser.AcaoContext,i):
        return str(ctx.ID()) +": { path:" +str(ctx.path().CADEIA()) + "}," + self.visitRecur_acao(ctx.recur_acao(),self.imageCounter)


    def visitRecur_acao(self, ctx: tileParser.Recur_acaoContext,i):
        self.acaoCounter+=1
        return "\n"+self.visitAcao(ctx.acao(),i) if ctx.acao() is not None else ''

    def visitRecur_tiles(self, ctx: tileParser.Recur_tilesContext):
        self.imageCounter+=1
        return "\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


    def getCodigo(self):
        return self.final
