def getProduction(c):
    if(c==1):
        return ['line','pgm']
    elif(c==2):
        return ['EOF']
    elif(c==3):
        return ['line_num','stmt']
    elif(c==4):
        return ['asgmnt']
    elif(c==5):
        return ['if']
    elif(c==6):
        return ['print']
    elif(c==7):
        return ['goto']
    elif(c==8):
        return ['stop']
    elif(c==9):
        return ['id','=','exp']
    elif(c==10):
        return ['term','exp*']    
    elif(c==11):
        return ['+','term']
    elif(c==12):
        return ['-','term']
    elif(c==13):
        return []
    elif(c==14):
        return ['id']
    elif(c==15):
        return ['const']
    elif(c==16):
        return ['IF','cond','line_num']
    elif(c==17):
        return ['term','cond*']    
    elif(c==18):
        return ['<','term']
    elif(c==19):
        return ['=','term']
    elif(c==20):
        return ['PRINT','id']
    elif(c==21):
        return ['GOTO','line_num']
    elif(c==22):
        return ['STOP']

def parseTable(m,n):

    row = ['pgm','line','stmt','asgmnt','exp','exp*','term','if','cond','cond*','print','goto','stop']
    col = ["EOF","line_num","id","=","+","-","const","IF","<","PRINT","GOTO","STOP","$"]
    m0 = row.index(m)
    n0 = col.index(n)
    parset = [
                [2,1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,3,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,4,-1,-1,-1,-1,5,-1,6,7,8,-1],
                [-1,-1,9,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,10,-1,-1,-1,10,-1,-1,-1,-1,-1,-1],
                [13,13,-1,-1,11,12,-1,-1,-1,-1,-1,-1,-1],
                [-1,-1,14,-1,-1,-1,15,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,16,-1,-1,-1,-1,-1],
                [-1,-1,17,-1,-1,-1,17,-1,-1,-1,-1,-1,-1],
                [-1,-1,-1,19,-1,-1,-1,-1,18,-1,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,20,-1,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,21,-1,-1],
                [-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1,22,-1]

              ] 
    return parset[m0][n0]
