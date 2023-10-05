import ply.lex as lex
import pathlib

# # Analisis Lexico
# reservadas = [
#     'PROGRAM',
#     'INT',
#     'FLOAT',
#     'IF',
#     'ELSE',
#     'READ',
#     'VOID',
#     'RETURN',
#     'FOR',
#     'WHILE',
#
# ]
#
# tokens = reservadas + [
#
#     # ; { } , = ( ) [ ]
#     'SEMICOLON', 'L_BRACE', 'R_BRACE',
#     'COMMA', 'ASSIGN', 'L_PARENTHESIS', 'R_PARENTHESIS',
#     'L_BRACKET', 'R_BRACKET',
#
#     # operators + - * /
#     'PLUS', 'MINUS', 'MULT', 'DIV',
#
#     # bool > < != == && ||
#     'GREATER_THAN', 'LESS_THAN', 'DIFF_THAN',
#     'EQUALS_TO', 'AND', 'OR',
#
#     # Constants
#     'CONST_ID', 'CONST_INT', 'CONST_FLOAT'
# ]

reservadas = [
    'PROGRAM',
    'ID',
    'INT',
    'FLOAT',
    'CHAR',
    'IF',
    'ELSE',
    'READ',
    'PRINT',
    'VOID',
    'RETURN',
    'FOR',
    'WHILE',
    'AVG',
    'MEDIAN',
    'MODE',
    'MAX',
    'MIN',
    'STDEV',
    'HIST',
    'COLOR',
    'BINS',
    'EDGECOLOR',
    'PLT',
    'XLABEL',
    'YLABEL',
    'TITLE',
    'SHOW',
    'BEGIN',
    'ENDFUN',
    'VAR',
    'MAIN'
]
tokens = reservadas + [

    # ; { } , = ( ) [ ]
    'SEMICOLON', 'L_BRACE', 'R_BRACE',
    'COMMA', 'ASSIGN', 'LP', 'RP',
    'LB', 'RB',

    # operators + - * /
    'PLUS',	'MINUS', 'MULT', 'DIV',

    # bool > < != == && ||
    'GT', 'LT', 'DIFF',
    'EQUALS', 'AND', 'OR',

    # Constants
     'CONST_INT', 'CONST_FLOAT', 'CONST_CHAR', 'LETRERO'
]

t_ignore = ' \t\n'

# bool > < != == && ||
t_GT = r'\>'
t_LT = r'\<'
t_DIFF = r'\!='
t_ASSIGN = r'='
t_EQUALS = r'=='
t_AND = r'&&'
t_OR = r'\|\|'

# Operators + - * /
t_PLUS = r'\+'
t_MINUS = r'\-'
t_MULT = r'\*'
t_DIV = r'/'

# ;  { } , = ( ) [ ]
t_SEMICOLON = r';'
t_L_BRACE = r'\{'
t_R_BRACE = r'\}'
t_COMMA = r','
t_LB = r'\['
t_RB = r'\]'
t_LP = r'\('
t_RP = r'\)'

def t_newLine(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_LETRERO(t):
    r'\"[a-zA-Z][a-zA-z0-9_ ]*\"'
    return t

def t_COMMENT(t):
    r'\#.*'
    pass

def t_CONST_FLOAT(t):
    r'\d\.\d+'
    t.value = float(t.value)
    return t


def t_CONST_INT(t):
    r'\d+'
    t.value = int(t.value)
    return t


def t_ID(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    if t.value.upper() in reservadas:
        t.value = t.value.upper()
        t.type = t.value
    return t


def t_error(t):
    print("caracter ilegal''%s'" % t.value[0])
    t.lexer.skip(1);




codigo = pathlib.Path("codigo.txt").read_text(encoding="utf-8")

lexer = lex.lex()
lexer.input(codigo)

while True:
    tok = lexer.token()
    if not tok: break
    print(tok)

