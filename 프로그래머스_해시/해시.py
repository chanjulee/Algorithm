#딕셔너리 만들기,추가,삭제,사용
def dictionary():
    #key 값이 중복되면 하나빼고 무시됨
    #key 값은 리스트 못 씀
    dic = dict() #빈 딕셔너리
    dic = {'name':'Hong', 'phone':'12345678', 'birth':'1218'}

    #딕셔너리 쌍 추가하기
    dic['e-mail'] = ['123@gmail','456@naver']

    #딕셔너리 요소 삭제하기
    del dic['birth']

    #딕셔너리에서 key 사용해 value 얻기
    print(dic['name'])

#딕셔너리 관련 함수들
def dictionaryfunction():
    #key 리스트 만들기 : keys()
    dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
    #dict_keys 객체 생성
    #리스트처럼 보이지만 append,insert,pop,remove,sort 사용불가
    print(dic.keys())
    #dict_keys 객체 리스트로 변환
    dicKeysList = list(dic.keys())
    dicKeysList.append('추가')

    #value 리스트 만들기 : values()
    print(dic.values())

    #key,value 쌍 얻기 : items()
    print(dic.items())

    #key:value 쌍 모두 지우기 : clear()
    #dic.clear()
    #print(dic)
    
    #key로 value 얻기 : get(key)
    print(dic.get('name'))
    print(dic.get('nokey')) #None 반환
    #print(dic['nokey']) #KeyError 발생
    
    #key 값이 없을 경우 디폴트 값 반환
    print(dic.get('nokey','key값없음'))
    #print(dic['nokey']) #값이 생기는것 아님

    #해당 key가 딕셔너리 안에 있는지 조사 : in
    print('name' in dic) #True
    print('nokey' in dic) #False

#딕셔너리 정렬해보기
def dictionarySort():
    #dict() 순서가 없는 자료형
    #sort() 안됨. sorted()로.
    dic = {'JS':[19,180], 'JN':[21,176], 'CL':[20,178], 'RJ':[21,170], 'JM':[21,176]}

    #dict() key 기준으로 정렬하기
    dicSorted = sorted(dic.keys(), key=lambda x: x) #이름순(key) 정렬. 이름만
    print(dicSorted)
    dicSorted = sorted(dic.items(), key=lambda x: x[0]) #이름순(key) 정렬. 쌍으로
    print(dicSorted)
    
    #dict() value 기준으로 정렬하기
    dicSorted = sorted(dic.values(), key=lambda x: x[0]) #나이순 정렬. value값만
    print(dicSorted)
    dicSorted = sorted(dic.values(), key=lambda x: x[1]) #키순 정렬. value값만
    print(dicSorted)
    dicSorted = sorted(dic.items(), key=lambda x: (x[1][0],x[0])) #나이순,이름순
    print(dicSorted)

if __name__ == "__main__":
    #dictionary()
    #dictionaryfunction()
    dictionarySort()


#출처 https://wikidocs.net/16#key-value