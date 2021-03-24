'''import sys
if __name__=="__main__":
    n = sys.stdin.readline().rstrip()
    num = [0]*9
    for x in n:
        x = int(x)
        if x==6 or x==9:
            num[6] += 1
        else:
            num[x] += 1
    num[6] = (num[6]+1)//2
    print(max(num))'''


import sys
if __name__=="__main__":
    n = str(sys.stdin.readline().rstrip())
    card = [1,1,1,1,1,1,2,1,1]
    count = 1

    if len(n)==1:
        print(count)
        sys.exit()
    for x in n:
        x = int(x)
        if x==9: 
            x = 6
        if card[x]>0:
            card[x] -= 1
        else:
            for i in range(9):
                if i==6:
                    card[i] += 2
                else:
                    card[i] += 1
            count += 1
            card[x] -= 1
    print(count)    
  