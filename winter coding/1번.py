def deliver(Instock, delivery):
    temp = []
    for d in delivery:
        if d[2]==1:
            Instock[d[0]-1] = 'O'
            Instock[d[1]-1] = 'O'
            continue        
        if d[2]==0:
            if Instock[d[0]-1]=='O':
                Instock[d[1]-1] = 'X'
            elif Instock[d[1]-1]=='O':
                Instock[d[0]-1] = 'X'
            elif Instock[d[0]-1]=='?' and Instock[d[1]-1]=='?':
                temp.append(d)
    if len(temp)!=0: return deliver(Instock, temp)
    else: return Instock

def solution(n, delivery):
    Instock = ['?']*n
    Instock = deliver(Instock, delivery)            
    return ''.join(Instock)