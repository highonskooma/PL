
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = "ELSE END EQUALS FALSE IF INT JUMP NOTEQUALS TRUE id numComandos : ComandoComandos : Comandos ComandoComando : ExprRComando : DeclaracaoComando : AtribuicaoComando : IFELSEFactor : numFactor : '-' numFactor : idFactor : TRUEFactor : FALSEFactor : '(' ExprR ')'ExprR : Expr '<' ExprExprR : Expr '>' ExprExprR : Expr EQUALS ExprExprR : Expr NOTEQUALS ExprExprR : ExprExpr : TermoExpr : Expr '+' TermoExpr : Expr '-' TermoTermo : FactorDeclaracao : INT idAtribuicao : id '=' ExprRAtribuicoes : AtribuicaoAtribuicoes : Atribuicoes AtribuicaoIFELSE : IF '(' ExprR ')' '{' Atribuicoes '}' ELSE '{' Atribuicoes '}'IFELSE : IF '(' ExprR ')' '{' Atribuicoes '}'"
    
_lr_action_items = {'INT':([0,1,2,3,4,5,6,7,9,12,14,15,16,17,18,25,29,30,31,32,33,34,35,36,37,39,45,50,],[8,8,-1,-3,-4,-5,-6,-17,-9,-18,-21,-7,-10,-11,-2,-22,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'id':([0,1,2,3,4,5,6,7,8,9,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,41,42,43,45,46,48,49,50,],[9,9,-1,-3,-4,-5,-6,-17,25,-9,29,-18,-21,-7,-10,-11,-2,29,29,29,29,29,29,-22,29,29,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,44,44,-24,-27,-25,44,44,-26,]),'IF':([0,1,2,3,4,5,6,7,9,12,14,15,16,17,18,25,29,30,31,32,33,34,35,36,37,39,45,50,],[10,10,-1,-3,-4,-5,-6,-17,-9,-18,-21,-7,-10,-11,-2,-22,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'num':([0,1,2,3,4,5,6,7,9,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,45,50,],[15,15,-1,-3,-4,-5,-6,-17,-9,15,-18,30,-21,-7,-10,-11,-2,15,15,15,15,15,15,-22,15,15,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'-':([0,1,2,3,4,5,6,7,9,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,45,50,],[13,13,-1,-3,-4,-5,-6,24,-9,13,-18,-21,-7,-10,-11,-2,13,13,13,13,13,13,-22,13,13,-9,-8,24,24,24,24,-19,-20,-23,-12,-27,-26,]),'TRUE':([0,1,2,3,4,5,6,7,9,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,45,50,],[16,16,-1,-3,-4,-5,-6,-17,-9,16,-18,-21,-7,-10,-11,-2,16,16,16,16,16,16,-22,16,16,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'FALSE':([0,1,2,3,4,5,6,7,9,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,45,50,],[17,17,-1,-3,-4,-5,-6,-17,-9,17,-18,-21,-7,-10,-11,-2,17,17,17,17,17,17,-22,17,17,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'(':([0,1,2,3,4,5,6,7,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,39,45,50,],[11,11,-1,-3,-4,-5,-6,-17,-9,27,11,-18,-21,-7,-10,-11,-2,11,11,11,11,11,11,-22,11,11,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'$end':([1,2,3,4,5,6,7,9,12,14,15,16,17,18,25,29,30,31,32,33,34,35,36,37,39,45,50,],[0,-1,-3,-4,-5,-6,-17,-9,-18,-21,-7,-10,-11,-2,-22,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,-27,-26,]),'<':([7,9,12,14,15,16,17,29,30,35,36,39,],[19,-9,-18,-21,-7,-10,-11,-9,-8,-19,-20,-12,]),'>':([7,9,12,14,15,16,17,29,30,35,36,39,],[20,-9,-18,-21,-7,-10,-11,-9,-8,-19,-20,-12,]),'EQUALS':([7,9,12,14,15,16,17,29,30,35,36,39,],[21,-9,-18,-21,-7,-10,-11,-9,-8,-19,-20,-12,]),'NOTEQUALS':([7,9,12,14,15,16,17,29,30,35,36,39,],[22,-9,-18,-21,-7,-10,-11,-9,-8,-19,-20,-12,]),')':([7,12,14,15,16,17,28,29,30,31,32,33,34,35,36,38,39,],[-17,-18,-21,-7,-10,-11,39,-9,-8,-13,-14,-15,-16,-19,-20,40,-12,]),'}':([7,12,14,15,16,17,29,30,31,32,33,34,35,36,37,39,42,43,46,49,],[-17,-18,-21,-7,-10,-11,-9,-8,-13,-14,-15,-16,-19,-20,-23,-12,45,-24,-25,50,]),'+':([7,9,12,14,15,16,17,29,30,31,32,33,34,35,36,39,],[23,-9,-18,-21,-7,-10,-11,-9,-8,23,23,23,23,-19,-20,-12,]),'=':([9,44,],[26,26,]),'{':([40,47,],[41,48,]),'ELSE':([45,],[47,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Comandos':([0,],[1,]),'Comando':([0,1,],[2,18,]),'ExprR':([0,1,11,26,27,],[3,3,28,37,38,]),'Declaracao':([0,1,],[4,4,]),'Atribuicao':([0,1,41,42,48,49,],[5,5,43,46,43,46,]),'IFELSE':([0,1,],[6,6,]),'Expr':([0,1,11,19,20,21,22,26,27,],[7,7,7,31,32,33,34,7,7,]),'Termo':([0,1,11,19,20,21,22,23,24,26,27,],[12,12,12,12,12,12,12,35,36,12,12,]),'Factor':([0,1,11,19,20,21,22,23,24,26,27,],[14,14,14,14,14,14,14,14,14,14,14,]),'Atribuicoes':([41,48,],[42,49,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Comandos","S'",1,None,None,None),
  ('Comandos -> Comando','Comandos',1,'p_Comandos_comando','tp2_yacc.py',25),
  ('Comandos -> Comandos Comando','Comandos',2,'p_Comandos_comandos_comando','tp2_yacc.py',30),
  ('Comando -> ExprR','Comando',1,'p_Comando_ExprR','tp2_yacc.py',35),
  ('Comando -> Declaracao','Comando',1,'p_Comando_Declaracao','tp2_yacc.py',40),
  ('Comando -> Atribuicao','Comando',1,'p_Comando_Atribuicao','tp2_yacc.py',44),
  ('Comando -> IFELSE','Comando',1,'p_Comando_IFELSE','tp2_yacc.py',48),
  ('Factor -> num','Factor',1,'p_Factor_num','tp2_yacc.py',54),
  ('Factor -> - num','Factor',2,'p_Factor_num_negativo','tp2_yacc.py',60),
  ('Factor -> id','Factor',1,'p_Factor_id','tp2_yacc.py',66),
  ('Factor -> TRUE','Factor',1,'p_Factor_TRUE','tp2_yacc.py',73),
  ('Factor -> FALSE','Factor',1,'p_Factor_FALSE','tp2_yacc.py',78),
  ('Factor -> ( ExprR )','Factor',3,'p_Factor_ExprR','tp2_yacc.py',83),
  ('ExprR -> Expr < Expr','ExprR',3,'p_ExprR_Expr_menor','tp2_yacc.py',88),
  ('ExprR -> Expr > Expr','ExprR',3,'p_ExprR_Expr_maior','tp2_yacc.py',97),
  ('ExprR -> Expr EQUALS Expr','ExprR',3,'p_ExprR_Expr_igual','tp2_yacc.py',106),
  ('ExprR -> Expr NOTEQUALS Expr','ExprR',3,'p_ExprR_Expr_diferente','tp2_yacc.py',112),
  ('ExprR -> Expr','ExprR',1,'p_ExprR_Expr','tp2_yacc.py',117),
  ('Expr -> Termo','Expr',1,'p_Expr_Termo','tp2_yacc.py',122),
  ('Expr -> Expr + Termo','Expr',3,'p_Expr_Termo_ADD','tp2_yacc.py',127),
  ('Expr -> Expr - Termo','Expr',3,'p_Expr_Termo_SUB','tp2_yacc.py',133),
  ('Termo -> Factor','Termo',1,'p_Termo_Factor','tp2_yacc.py',139),
  ('Declaracao -> INT id','Declaracao',2,'p_Declaracao','tp2_yacc.py',145),
  ('Atribuicao -> id = ExprR','Atribuicao',3,'p_Atribuicao','tp2_yacc.py',155),
  ('Atribuicoes -> Atribuicao','Atribuicoes',1,'p_Atribuicoes_Atribuicao','tp2_yacc.py',162),
  ('Atribuicoes -> Atribuicoes Atribuicao','Atribuicoes',2,'p_Atribuicoes_Atribuicao_Varias','tp2_yacc.py',167),
  ('IFELSE -> IF ( ExprR ) { Atribuicoes } ELSE { Atribuicoes }','IFELSE',11,'p_IF_ELSE','tp2_yacc.py',173),
  ('IFELSE -> IF ( ExprR ) { Atribuicoes }','IFELSE',7,'p_IFELSE','tp2_yacc.py',185),
]
