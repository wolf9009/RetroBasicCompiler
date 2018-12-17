import re
import sys
from pSet import getProduction,parseTable
global file;

def openfile(filename):
    file = open(filename,'r')
    return file

def checkLineNo(token):
    if(not token.isdigit()):
        raise NameError(token + ' is not a digit. line_no must be a digit')
    else:
        digit = int(token)
        if(digit >= 1 and digit <=1000):
            return ['line_num',token]
        else:
            raise NameError(token + ' is a not in a valid range')

def checkToken(token):
    if(token == '<'):
        return ['<',token]
    elif (token == '='):
        return ['=',token]
    elif (token == ''):
        return 
    elif (token == '+'):
        return ['+',token]
    elif (token == '-'):
        return ['-',token]
    elif (token == 'GOTO'):
        return ['GOTO',token]
    elif (token == 'PRINT'):
        return ['PRINT',token]
    elif (token == 'STOP'):
        return ['STOP',token]
    elif (token == 'IF'):
        return ['IF',token]
    else:
        if(token.isdigit()):
            if(int(token) <= 100 and int(token) >= 0):
                return ['const',token]
            else:
                raise NameError(token + ' is a not in a valid range')
        else:
            checker = re.compile('[A-Z]')
            if(checker.match(token) and len(token)==1):
                return ['id',token]
            else:
                raise NameError('Token error: not a valid identifier '+ token)

def scanner(argv=''):
    filename = 'input.txt' or argv 
    file = openfile(filename)
    tokenizefile = list()
    for line in file:
        tokenizeline = list();
        tokens = line.strip().split(' ')
        tokens[-1] = tokens[-1].strip('\n')
        for i in range(len(tokens)):
            if(i==0):
                x = checkLineNo(tokens[i])
                tokenizeline.append(x) 
            else:
                x = checkToken(tokens[i])
                tokenizeline.append(x)
        if(tokens[1] == 'GOTO' or tokens[1] == 'IF'):
            if(tokenizeline[-1][1].isnumeric() and int(tokenizeline[-1][1]) >= 1 and int(tokenizeline[-1][1]) <=1000):
                tokenizeline[-1][0] = 'line_num'
        tokenizefile.append(tokenizeline)
    tokenizefile.append([['EOF','EOF']])
    return tokenizefile

def getNewList(lists):
    newlist = []
    for list in lists:
        for lis in list:
            newlist.append(lis)
    return newlist

def isTerminal(s):
    prod_set = set(['pgm','line','stmt','asgmnt','exp','exp*','term','if','cond','cond*','print','goto','stop'])
    return not (s in prod_set)
    
def parser():
    tokenizeline = scanner()

    tokenizeline = getNewList(tokenizeline)

    stack = list()
    stack.append('$')
    stack.append('pgm')

    i = 0
    e = 1

    while(stack[-1] != '$' and i != len(tokenizeline)):
        if(isTerminal(stack[-1]) and tokenizeline[i][0] == stack[-1]):
            stack.pop()
            i+=1
        elif(not isTerminal(stack[-1])  and isTerminal(tokenizeline[i][0])):
            #if(not parseTable(stack[-1],tokenizeline[i][0]) == 23 and not parseTable(stack[-1],tokenizeline[i][0]) == 24):
            if(not parseTable(stack[-1],tokenizeline[i][0]) == -1):
                nl = getProduction(parseTable(stack[-1],tokenizeline[i][0]))
                stack.pop()
                
                for k in reversed(nl):
                    stack.append(k)
                    
            else:
                print("Error in parsing : ", tokenizeline[i][1])
                e = 0
                break

        elif(stack[-1] == '$' and tokenizeline[i][0] == '$'):
            print("Accept parsing")
            e = 1 
        else:
            print("Error in parsing : ", tokenizeline[i][1])
            e = 0
            break
    if(e==0):
        return False
    else:
        return True

def changeOne(x):
    if(x=='line_num'):
        return 10
    elif(x=='id'):
        return 11
    elif(x=='const'):
        return 12
    elif(x=='IF'):
        return 13
    elif(x=='GOTO'):
        return 14
    elif(x=='PRINT'):
        return 15
    elif(x=='STOP'):
        return 16
    elif(x in set(['+','-','<','='])):
        return 17
    elif(x=='EOF'):
        return 0


def changeTwo(x):
    if(x=='STOP' or x=='PRINT' or x=='IF'):
        return 0
    elif(x=='+'):
        return 1
    elif(x=='-'):
        return 2
    elif(x=='<'):
        return 3
    elif(x=='='):
        return 4
    elif((re.compile('[A-Z]')).match(x) and len(x)==1):
        return ord(x)-64
    else:
        return x

if(parser()):
    tokenizeline = scanner()
    for line in tokenizeline:
        for token in line:
            token[0] = changeOne(token[0])
            token[1] = changeTwo(token[1])
    for i in range(len(tokenizeline)-1):
        if(tokenizeline[i][1][0] == 13 or tokenizeline[i][1][0] == 14):
            tokenizeline[i][-1][0] = 14
    z = list()
    for line in tokenizeline:
        for token in line:
            if(token[1] != 'GOTO'):
                z.append(int(token[0]))
                if(token[1] != 'EOF'):
                    z.append(int(token[1]))             
    f = open("output.txt", "w+")
    result = ' '.join(str(e) for e in z)
    f.write(result.strip())
    print("***Export output B-code in file: output.txt*** \nB-CODE OUTPUT:\n"+result.strip())
    f.close()
else:
    print("Parse Failed")