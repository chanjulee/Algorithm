def solution(s):
    answer = 0
    for i in range(1,len(s)//2+1):
        ret = ''#각 분할당 비교할 문자열
        counter = 1
        prev = s[:i]#이전 문자열

        for j in range(i, len(s)+i, i):
            if prev==s[j:j+i]:
                count+=1
            else:
                if counter!=1:
                    ret=ret+str(counter)+prev
                else:
                    ret=ret+prev
                prev = s[j:j+i]
                count=1
        answer = min(answer,len(ret))



    return min(answer,len(s))

s="aabbaccc"
print(solution(s))