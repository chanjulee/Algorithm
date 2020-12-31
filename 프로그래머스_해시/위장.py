def solution(clothes):
    dic = dict() #dic={}
    for c in clothes: #c:[의상이름,의상종류]
        dic[c[1]] = dic.get(c[1],0)+1 #의상종류 사전
    answer = 1
    for x in dic.values():
        answer *= x+1 #x+1:종류에서뽑는경우+안뽑는경우
    return answer-1 #-1:아무것도 안뽑은 경우