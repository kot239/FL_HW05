import ply.lex as lex 

tokens = [
    'LIT',  
    'SEN',
    'CON',
    'DIS',
    'OPENBR',
    'CLOSEBR',
    'DOT'
]

t_LIT = r'[a-zA-Z_][A-Za-z_0-9]*'
t_SEN = r'\:\-'
t_CON = r'\,'
t_DIS = r'\;'
t_OPENBR = r'\('
t_CLOSEBR = r'\)'
t_DOT = r'\.'

t_ignore = ' \t'

def t_newline(t): 
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_error(t): 
    print("Illegal character {0} at line {1} in pos {2}".format(t.value[0], t.lineno, t.lexpos))
    tokenize.lex_error = True
    t.lexer.skip(1)
