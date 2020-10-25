def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=lambda x: len(x))
    #print(s)
    for x in s:
        x = x.split(',')
        for y in x:
            if int(y) not in answer:
                answer.append(int(y))
    return answer
    

s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
print(solution(s))