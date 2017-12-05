from ANTLR.tileVisitor import *
from ANTLR.tileParser import *

class GeradorCodigo(tileVisitor):

    #Array que armazena as imagens

    imageArray = []
    imageCounter = 0

    final = """<!DOCTYPE html><html><head><script type="text/javascript">var ctx = null;size = {size}
    var i = 0;
    var gameMap = new Array();

    for(i=0;i<={size}*{size};i++){
        gameMap[i] = 0;
    }
    /*Tile Loading */
    var image = new Array();
    {tiles}

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
        return "image["+str(self.imageCounter)+"].src = " +str(ctx.path().CADEIA()) + self.visitRecur_tiles(ctx.recur_tiles())



    def visitRecur_tiles(self, ctx: tileParser.Recur_tilesContext):
        self.imageCounter+=1
        return ";\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


    def getCodigo(self):
        return self.final
