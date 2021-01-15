#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
#모든 범위를 포함하는 리스트 선언(모든 값은 0 초기화)
count = [0] * (max(array)+1)

for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 해당하는 인덱스 값 증가
for i in range(len(count)):
    for j in range(count[i]):#등장한 횟수만큼 인덱스 출력
        print(i,end=' ')

'''
계수 정렬
O(N+K)
각각의 계수가 몇번 등장했는지 카운트하는 방법
동일한 값을 가지는 데이터가 여러개 등장할 때 효과적
ex)같은 성적을 맞은 학생이 많을 때
'''