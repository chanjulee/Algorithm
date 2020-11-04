def solution(answers):
    answer = []    
    a = [1,2,3,4,5]*2000
    b = [2,1,2,3,2,4,2,5]*1250
    c = [3,3,1,1,2,2,4,4,5,5]*1000
    score = [[1,0],[2,0],[3,0]]
    
    i = 0    
    for ans in answers:
        if ans==a[i]:
            score[0][1]+=1
        if ans==b[i]:
            score[1][1]+=1
        if ans==c[i]:
            score[2][1]+=1
        i+=1
        
    sorted(score, key=lambda x:-x[1])
    answer.append(score[0][0])
    for sco in score:
        if sco==score[0][0]:
            answer.append(sco)        
    return answer

answers=[1,2,3,4,5]
solution(answers)