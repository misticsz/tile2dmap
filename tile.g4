grammar tile;

ID :      ('a'..'z' | 'A'..'Z' | '_') ('a'..'z' | 'A'..'Z' | '0'..'9' | '_')*;
NUM_INT :    ('0'..'9')+;
NUM_REAL :   ('0'..'9')+ '.' ('0'..'9')+;
CADEIA :     '"' ~('\n' | '\r' | '"')* '"';
WS : 		 [ \n\t\r]+ -> skip;

/* Bloco principal */

mapa:
	'map' '(' size ')' '{' 'import' '{' tile? '}' 'commands' ('{'commands?'}')? '}' EOF;

/* Comandos para se utilizar para preencher / alterar o mapa , podem ser dinamicos(especiais)
   se forem criadas acoes anteriormente na importacao de tiles */

commands:
  (add | remove | especial | loop) recur_commands ;

recur_commands:  commands | ;

/* Melhorar loop apenas X e Y */

loop:
    'preencher' ('horizontal' | 'vertical') n1=NUM_INT 'ate' n2=NUM_INT ID;
add:
    'add' ID 'position' '(' n1=NUM_INT n2=NUM_INT ')';
remove:
    'remove' ID 'position' '(' n1=NUM_INT n2=NUM_INT ')';
especial:
    c1=ID c2=ID 'position' '(' n1=NUM_INT n2=NUM_INT ')';

tile:
    ID '{' path nivel? acao? '}' recur_tiles;

acao:
  'acao' '{' ID '{' path '}' '}' recur_acao;

recur_acao:
  acao | ;

recur_tiles:
    tile | ;

size:
  'size' ':' NUM_INT;

nivel:
  'nivel' ':' NUM_INT;

path:
  'path' ':' CADEIA;
