from lexer import *
import ply.yacc as yacc 
import sys
import re

def p_sentence(p):
    '''
        sentence : atom SEN disj DOT sentence
                 | atom DOT sentence
                 | atom SEN disj DOT 
                 | atom DOT 
    '''
    if len(p) == 6:
        p[0] = 'HEAD( ' + p[1] + ' ) BODY( ' + p[3] + ' )\n' + p[5]
    elif len(p) == 4:
        p[0] = 'HEAD( ' + p[1] + ' )\n' + p[3]
    elif len(p) == 5:
        p[0] = 'HEAD( ' + p[1] + ' ) BODY( ' + p[3] + ' )'
    else:
        p[0] = 'HEAD( ' + p[1] + ' )'

def p_disj(p):
    '''
        disj : conj DIS disj
             | conj
    '''
    if len(p) == 4:
        p[0] = 'DISJ ( ' + p[1] + ' )  ( ' + p[3] + ' )'
    else:
        p[0] = p[1]

def p_conj(p):
    '''
        conj : subatom CON conj
             | subatom 
    '''
    if len(p) == 4:
        p[0] = 'CONJ ( ' + p[1] + ' )  ( ' + p[3] + ' )'
    else:
        p[0] = p[1]

def p_subatom(p):
    '''
        subatom : OPENBR disj CLOSEBR
                | atom
             
    '''
    if len(p) == 4:
        p[0] = '( ' + p[2] + ' )'
    else:
        p[0] = p[1]

def p_atom(p):
    '''
        atom : LIT seq
             | LIT 
    '''
    if len(p) == 3:
        p[0] = '(ATOM ' + p[1] + ' ' + p[2] + ' )'
    else:
        p[0] = '(ATOM ' + p[1] + ')'

def p_seq(p):
    '''
        seq : OPENBR atombr CLOSEBR seq
            | OPENBR atombr CLOSEBR
            | LIT seq
            | LIT
    '''
    if len(p) == 5:
        p[0] = '( ' + p[2] + ' )' + p[4]
    elif len(p) == 4:
        p[0] = '( ' + p[2] + ' )'
    elif len(p) == 3:
        p[0] = '(ATOM ' + p[1] + ') ' +  p[2]
    else:
        p[0] = '(ATOM ' + p[1] + ')'

def p_atombr(p):
    '''
        atombr : OPENBR atombr CLOSEBR
               | atom
    '''
    if len(p) == 4:
        p[0] = '( ' + p[2] + ' )'
    else:
        p[0] = p[1]

def p_error(p):
    raise Exeception


def parse_file(file_name):
    lexer = lex.lex()
    parser = yacc.yacc()

    input_file = open(file_name)
    inp = input_file.read()
    input_file.close()

    output_file = open(file_name + '.out', 'w')

    regex = re.compile(r'^[ \n\t]*$')
    if regex.match(inp):
        output_file.write("Empty file")
        output_file.close()
        return True

    try:
        outp = parser.parse(inp)
    except:
        output_file.write("Can't build syntax tree")
        output_file.close()
        return False

    output_file.write(outp)
    output_file.close()
    return True

if __name__ == "__main__":
    parse_file(sys.argv[1])