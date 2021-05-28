import ply.yacc as yacc
from tp2_lex import tokens
#from calc_lex import literals
import sys

#Data Structure
#key : string (nome da variavel)
#valor : endereço da stack
atribs = {}

#Contador de atribuições
atrib_counter = 0

#Output file with VM instructions
out = open("output.vm","w+")

out.write("START\n")

#Get the token map from the lexer. this is required

#Production rules
#Comandos
def p_Comandos_comando(p):
    "Comandos : Comando"
    out.write(p[1]+"\n")

def p_Comandos_comandos_comando(p):
    "Comandos : Comandos Comando"
    out.write(p[2]+"\n")

def p_Comando_ExprR(p):
    "Comando : ExprR"
    p[0] = p[1]

def p_Comando_Declaracao(p):
    "Comando : Declaracao"
    p[0] = p[1]    

def p_Comando_Atribuicao(p):
    "Comando : Atribuicao"
    p[0] = p[1] 

def p_Comando_IFELSE(p):
    "Comando : IFELSE"
    p[0] = p[1]   

def p_Factor_num(p):
    "Factor : num"
    p[0] = "PUSHI " + p[1] + "\n"

def p_Factor_num_negativo(p):
    "Factor : '-' num"
    p[0] = "PUSHI " + str((int(p[2])*(-1))) + "\n" 

def p_Factor_id(p):
    "Factor : id"
    p[0] = "PUSHG " + str(atribs[p[1]]) + "\n"

def p_Factor_TRUE(p):
    "Factor : TRUE"
    p[0] = "PUSHI 1\n"

def p_Factor_FALSE(p):
    "Factor : FALSE"
    p[0] = "PUSHI 0\n"  

def p_Factor_ExprR(p):
    "Factor : '(' ExprR ')'"
    p[0] = p[2]      

def p_ExprR_Expr_menor(p):
    "ExprR : Expr '<' Expr"
    p[0] = p[1] + p[3] + "INF\n"

def p_ExprR_Expr_maior(p):
    "ExprR : Expr '>' Expr"
    p[0] = p[1] + p[3] + "SUP\n"

def p_ExprR_Expr_igual(p):
    "ExprR : Expr EQUALS Expr"
    p[0] = p[1] + p[3] + "EQUAL\n"

def p_ExprR_Expr_diferente(p):
    "ExprR : Expr NOTEQUALS Expr"
    p[0] = p[1] + p[3] + "EQUAL NOT\n"

def p_ExprR_Expr(p):
    "ExprR : Expr"
    p[0] = p[1]

def p_Expr_Termo(p):
    "Expr : Termo"
    p[0] = p[1]

def p_Expr_Termo_ADD(p):
    "Expr : Expr '+' Termo"
    p[0] = p[1]+p[3]+"ADD\n"  

def p_Expr_Termo_SUB(p):
    "Expr : Expr '-' Termo"
    p[0] = p[1]+p[3]+"SUB\n"

def p_Termo_Factor(p):
    "Termo : Factor"
    p[0] = p[1]

def p_Declaracao(p):
    "Declaracao : INT id"
    p[0] = "PUSHI 0\n"
    global atribs
    global atrib_counter
    atribs[p[2]] = atrib_counter
    atrib_counter+=1

def p_Atribuicao(p):
    "Atribuicao : id '=' ExprR"
    global atribs
    p[0] = p[3] + "STOREG " + str(atribs[p[1]]) + "\n"

def p_Atribuicoes_Atribuicao(p):
    "Atribuicoes : Atribuicao"
    p[0] = p[1]

def p_Atribuicoes_Atribuicao_Varias(p):
    "Atribuicoes : Atribuicoes Atribuicao"
    p[0] = p[1] + p[2]

def p_IF_ELSE(p):
    "IFELSE : IF '(' ExprR ')' '{' Atribuicoes '}' ELSE '{' Atribuicoes '}'"
    p[0] = p[3]+ "\n" + "JZ IF0\n" + p[6] + "\nIF0:\n"

def p_IFELSE(p): 
    "IFELSE : IF '(' ExprR ')' '{' Atribuicoes '}'"
    p[0] = p[3]+ "\n" + "JZ IF0\n" + p[6] + "\nIF0:\n"

#error rule for syntax errors
def p_error(p):
    print("Syntax error in input:", p)

#buil the parser
parser = yacc.yacc()

#reading input
file = open("input.txt","r")
for linha in file:
    result = parser.parse(linha)
    print("Frase válida")

out.write("STOP")
out.close()    
