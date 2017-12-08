from ANTLR.tileVisitor import *
from ANTLR.tileParser import *

class GeradorCodigo(tileVisitor):

    #Array que armazena as imagens

    imageArray = []
    imageCounter = 0
    tileCounter = 0
    acaoCounter = 1
    size = ''
    text = ''


    final = """<!DOCTYPE html><html><head><script type="text/javascript">var ctx = null;size = {size}
    var i = 0;
    var gameMap = new Array();

    for(i=0;i<={size}*{size};i++){
        gameMap[i] = 0;
    }
    /*Tile Loading */
    var image = new Array();
    var tile = new Array();

    {tiles}

    {images}

    {commands}

    function findImageByName(name,tile,imageCounter){
    	var i = 0;
    	while(tile[i].nome!=name){
    		i++;
    	}
    	return i;
    }

    var currentSecond = 0, frameCount = 0, framesLastSecond = 0;
    window.onload = function()
    {
    	ctx = document.getElementById('game').getContext("2d");
    	requestAnimationFrame(drawGame);
    	ctx.font = "bold 10pt sans-serif";
    };


    """


    def visitMapa(self,ctx: tileParser.MapaContext):
        self.size = str(ctx.size().NUM_INT())
        self.final = self.final.replace('{size}',self.size)
        self.final = self.final.replace('{tiles}',str(self.visitTile(ctx.tile())))
        self.final = self.final.replace('{commands}',str(self.visitCommands(ctx.commands())))

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

    def visitCommands(self, ctx: tileParser.CommandsContext):

        if ctx.add() is not None:
            self.text += '\ngameMap['+str(int(ctx.add().n1.text)*(int(self.size))+(int(ctx.add().n2.text)))+'] = findImageByName('+str(ctx.add().ID())+',tile,'+str(self.imageCounter)+');'
        if ctx.remove() is not None:
            self.text += '\ngameMap['+str(int(ctx.remove().n1.text)*(int(self.size))+(int(ctx.remove().n2.text)))+'] = 0;'
        if ctx.loop() is not None:
            self.text += '\n\n/*Preencher*/\n var it;\n for(it='+str(ctx.loop().n1.text)+';i<'+str(ctx.loop().n2.text)+';it++){\n   gameMap[it] =  findImageByName('+str(ctx.loop().ID())+',tile,'+str(self.imageCounter)+');\n }'
        if ctx.especial() is not None:
            self.text += '\n image[findImageByName('+str(ctx.especial().c2.text)+',tile,'+str(self.imageCounter)+')].src = tile[findImageByName('+str(ctx.especial().c2.text)+',tile,'+str(self.imageCounter)+')].action.'+str(ctx.especial().c1.text)+'.path;'



        self.visitRecur_commands(ctx.recur_commands())

        return self.text;

    def visitRecur_commands(self, ctx: tileParser.Recur_commandsContext):
        return "\n"+self.visitCommands(ctx.commands()) if ctx.commands() is not None else ''

    def visitRecur_tiles(self, ctx: tileParser.Recur_tilesContext):
        self.imageCounter+=1
        return "\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


    def getCodigo(self):
        return self.final
