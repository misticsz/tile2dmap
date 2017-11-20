grammar tile;


CADEIA:
    '"' ~('\n' | '\r' | '"')* '"';

COMENTARIO:
    '//' ~('/' | '\n')* '\n' -> skip;

ESPACO:
    (' ' | '\t' | '\r' | '\n') -> skip;

ERRO: .;


INTEGER_NUMBER
:   [0-9]+;

COMMA   :   ',';

ID  :   ('a'..'z'|'A'..'Z'|'_') ('a'..'z'|'A'..'Z'|'0'..'9'|'_')*;

SPACE : (' ' | '\t' | '\r' | '\n') {skip();};

NAME
    : [a-zA-Z_][a-zA-Z_0-9]*
    ;

mapa:
	'map' '(' size ')' '{' tile? commands? '}' EOF;

commands:
  (add | remove | especial | loop) recur_commands ;

recur_commands:
    commands | ;


loop:
    'preencher de' INTEGER_NUMBER 'ate' INTEGER_NUMBER ID;
add:
    'add' ID 'position' '(' INTEGER_NUMBER INTEGER_NUMBER ')';
remove:
    'remove' ID 'position' '(' INTEGER_NUMBER INTEGER_NUMBER ')';
especial:
    ID 'position' '(' INTEGER_NUMBER INTEGER_NUMBER ')';

tile:
    'import tile' '{' ID '{' path nivel? acao? '}' '}' recur_tiles;

acao:
  'acao' '{' ID '{' path '}' '}' recur_acao;

recur_acao:
  acao | ;

recur_tiles:
    tile | ;

size:
  'size' ':' INTEGER_NUMBER;

nivel:
  'nivel' ':' INTEGER_NUMBER;

path:
  'path' ':' CADEIA;
