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
    text = ''
    size = ''
    tile = ''

    final = """<!DOCTYPE html><html><head><script type="text/javascript">var ctx = null;size = {size}
    var i = 0;
    var gameMap = new Array();

    function findImageByName(name,tile,imageCounter){
	var i = 0;
    var aux = 0;
	while(i<imageCounter){
		if(tile[i].name==name){
            aux=i;
        }
        i++;
	}
    return aux;
    }


    for(i=0;i<={size}*{size};i++){
        gameMap[i] = 0;
    }
    /*Tile Loading */
    var image = new Array();
    var tile = new Array();

    {tiles}


    {commands}


    var tileW = 17, tileH = 17;
    var mapW = {size}, mapH = {size};
    var currentSecond = 0, frameCount = 0, framesLastSecond = 0;
    var currentSecond = 0, frameCount = 0, framesLastSecond = 0;

    window.onload = function()
    {
    	ctx = document.getElementById('game').getContext("2d");
    	requestAnimationFrame(drawGame);
    	ctx.font = "bold 10pt sans-serif";
    };

    function drawGame()
    {

    	if(ctx==null) { return; }

    	var sec = Math.floor(Date.now()/1000);
    	if(sec!=currentSecond)
    	{
    		currentSecond = sec;
    		framesLastSecond = frameCount;
    		frameCount = 1;
    	}
    	else { frameCount++; }

    	for(var y = 0; y < mapH; ++y)
    	{
    		for(var x = 0; x < mapW; ++x)
    		{
    			switch(gameMap[((y*mapW)+x)])
    			{
                    {case}
    			}

    		}
    	}

    	ctx.fillStyle = "#ff0000";
    	ctx.fillText("-: " + framesLastSecond, 10, 20);

    	requestAnimationFrame(drawGame);
    }
    </script>

    </head>
    <body>

    <canvas id="game" width="1000" height="1000"></canvas>

    </body>
    </html>


    """


    def visitMapa(self,ctx: tileParser.MapaContext):
        self.size = str(ctx.size().NUM_INT())
        self.final = self.final.replace('{size}',self.size)
        self.final = self.final.replace('{tiles}',str(self.visitTile(ctx.tile())))
        self.final = self.final.replace('{case}',str(self.visitCase(ctx.tile())))
        self.final = self.final.replace('{commands}',str(self.visitCommands(ctx.commands())))

    def visitTile(self,ctx: tileParser.TileContext):
        path = str(ctx.path().CADEIA())
        name = str(ctx.ID())
        if ctx is not None:
            self.tile += "\n\ntile["+str(self.imageCounter)+"] = { \n path:"+path+", name:'"+name+"'"
            if ctx.acao() is not None:
                self.tile+=', action :{'+self.visitAcao(ctx.acao(),self.imageCounter) + "}"
            self.tile +='};'
            self.tile+="\nimage["+str(self.imageCounter)+"] = new Image(40,40);" + "\nimage["+str(self.imageCounter)+"].src = tile["+str(self.imageCounter)+"].path;"
            self.visitRecur_tiles(ctx.recur_tiles())

        return self.tile;

    def visitCase(self,ctx: tileParser.TileContext):
        if ctx is not None:
            case = ""
            for x in range(0, self.imageCounter):
                case += "case "+ str(x) +":\n ctx.drawImage(image["+str(x)+"],x*tileW,y*tileH);\n break;\n"
            return case

    def visitCommands(self, ctx: tileParser.CommandsContext):
        if ctx is not None:
            if ctx.add() is not None:
                self.text += '\ngameMap['+str(int(ctx.add().n1.text)*(int(self.size))+(int(ctx.add().n2.text)))+'] = findImageByName("'+str(ctx.add().ID())+'",tile,'+str(self.imageCounter)+');'
            if ctx.remove() is not None:
                self.text += '\ngameMap['+str(int(ctx.remove().n1.text)*(int(self.size))+(int(ctx.remove().n2.text)))+'] = 0;'
            if ctx.loop() is not None:
                if(ctx.loop().tipo.text=='linha'):
                    self.text += '\n\n/*Preencher*/\n var temp; \n var it;\n for(it='+str(ctx.loop().n1.text)+';it<'+str(ctx.loop().n2.text)+';it++){\n  temp = it+'+str(int(ctx.loop().cN.text)*(int(self.size)))+';\n gameMap[temp] =  findImageByName("'+str(ctx.loop().nome.text)+'",tile,'+str(self.imageCounter)+');\n }'
                if(ctx.loop().tipo.text=='coluna'):
                    self.text += '\n\n/*Preencher*/\n var temp; \n var it;\n for(it='+str(ctx.loop().n1.text)+';it<'+str(ctx.loop().n2.text)+';it++){\n  temp = it*'+str(int(self.size))+';\n gameMap[temp] =  findImageByName("'+str(ctx.loop().nome.text)+'",tile,'+str(self.imageCounter)+');\n }'

            if ctx.especial() is not None:
                self.text += '\n image[findImageByName("'+str(ctx.especial().c2.text)+'",tile,'+str(self.imageCounter)+')].src = tile[findImageByName("'+str(ctx.especial().c2.text)+'",tile,'+str(self.imageCounter)+')].action.'+str(ctx.especial().c1.text)+'.path;'

            self.visitRecur_commands(ctx.recur_commands())

            return self.text;
        return ''

    def visitRecur_commands(self, ctx: tileParser.Recur_commandsContext):
        return "\n"+self.visitCommands(ctx.commands()) if ctx.commands() is not None else ''


    def visitAcao(self,ctx: tileParser.AcaoContext,i):
        if ctx is not None:
            return str(ctx.ID()) +": { path:" +str(ctx.path().CADEIA()) + "}," + self.visitRecur_acao(ctx.recur_acao(),self.imageCounter)


    def visitRecur_acao(self, ctx: tileParser.Recur_acaoContext,i):
        self.acaoCounter+=1
        print(ctx.acao())
        return "\n"+self.visitAcao(ctx.acao(),i) if ctx.acao() is not None else ''

    def visitRecur_tiles(self, ctx: tileParser.Recur_tilesContext):
        self.imageCounter+=1
        return "\n"+self.visitTile(ctx.tile()) if ctx.tile() is not None else ''


    def getCodigo(self):
        return self.final
