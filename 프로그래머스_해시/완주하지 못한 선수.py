def solution(participant,completion):
    dic = dict()
    for p in participant: #이름별 참가자수
        dic[p] = dic.get(p,0)+1
    for c in completion: #완주한 참가자 이름빼기
        dic[c] = dic.get(c,0)-1
    for key,val in dic.items():
        if val!=0:
            return key
    return None

if __name__ == "__main__":
    P = ['mislav', 'kiki', 'mislav']
    C = ['mislav', 'kiki']
    print(solution(P,C))

'''
def solution(participant, completion):
    answer = ''
    dic=dict() #빈 딕셔너리
    for i in range(len(participant)):
        word=participant[i]
        dic[word]=dic.get(word,0)+1 #참가하면 +1 #get(word,0) word가 비어있으면 0을 가져온다...
    for i in range(len(completion)):
        word=completion[i]
        dic[word]=dic.get(word)-1 #완주하면 다시 -1 동명이인 포함 완주하면 0된다
    for key,val in dic.items():
        if val!=0:
            answer=key
            break
    return answer
'''