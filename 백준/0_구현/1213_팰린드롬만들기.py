import sys
def func(x,i,result,flag):
    if x>=(length-1):
        if length%2==1 and result[len(result)//2]=='':
            result[len(result)//2] = name[-1]
            return result
        else:
            return result
    if name[x]!=name[x+1]:
        if length%2==0:
            return "I'm Sorry Hansoo"
        if flag==False:
            flag = True
            result[len(result)//2] = name[x]
            return func(x+1,i,result,flag)
        else:
            return "I'm Sorry Hansoo"
    else:
        result[i] = name[x]
        result[-(i+1)] = name[x+1]
        return func(x+2,i+1,result,flag)

if __name__=="__main__":
    name = list(sys.stdin.readline().rstrip())
    name.sort()

    flag = False
    length = len(name)
    if length==1:
        print(name[0])
        sys.exit()
    result = ['']*(length)
    result = func(0,0,result,flag)
    for r in result:
        print(r,end='')

        #result += result[::-1]