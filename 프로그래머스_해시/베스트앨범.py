def solution(genres,plays):
    dic = dict()
    for index,(genre,play) in enumerate(zip(genres,plays)):
        dic[genre] = dic.get(genre,[0]) #장르사전 없으면 추가
        dic[genre][0] += play #재생횟수 추가 부분
        dic[genre].append([index,play])
    print(dic)
    
    answer = []
    dicSorted = sorted(dic.values(), key=lambda x:-x[0]) #총재생수 정렬
    for x in dicSorted: #총재생수 많은 장르순으로 접근
        x = x[1:] #재생부분 제거
        x.sort(key=lambda x: (-x[1],x[0])) #장르 내에서 정렬. 재생수,고유숫자순
        answer.append(x[0][0])
        if len(x)<2: continue #장르에 노래가 하나인 경우
        answer.append(x[1][0])
    
    return answer        

if __name__ == "__main__":
    g = ['classic','classic','classic','classic','pop']
    p = [500,150,800,800,2500]
    print(solution(g,p))