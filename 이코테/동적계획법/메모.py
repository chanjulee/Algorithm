'''
다이나믹 프로그래밍 사용조건
1. 최적 부분 구조 - 큰 문제를 작은 문제로 나눌 수 있으며,
    작은 문제의 답을 모아서 큰 문제를 해결
2. 중복되는 부분 문제 - 동일한 작은 문제를 반복적으로 해결
'''

#피보나치 수열(단순재귀)
def fibo(x):
    if x==1 or x==2: #바닥조건
        return 1
    return fibo(x-1) + fibo(x-2)

'''
메모이제이션
- 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
- 값을 기록해 놓은다는 점에서 캐싱(Cashing)
탑다운 방식 -하향식
보텀업 방식 -상향식
'''

#피보나치 수열(탑다운 dp)
d_td = [0] * 100
def fibo_topdown(x):
    if x==1 or x==2: #종료조건
        return 1
    if d_td[x]!=0: #이미계산한문제 반환
        return d_td[x]
    d_td[x] = fibo_topdown(x-1) + fibo_topdown(x-2)
    return d_td[x]
print(fibo_topdown(99))

#피보나치 수열(바텀업 dp)
d_bu = [0] * 100
d_bu[1] = 1 #첫번째 피보나치 수
d_bu[2] = 1 #두번째 피보나치 수
n = 99
for i in range(3, n+1): #피보나치를 반복문으로 구현
    d_bu[i] = d_bu[i-1] + d_bu[i-2]
print(d_bu[n])


'''
다이나믹 프로그래밍 vs 분할 정복
공통점 - 최적 부분 구조를 가질 때 사용할 수 있다
차이점 - 부분 문제의 중복
다이나믹 프로그래밍 유형 파악하기
1. 그리디, 구현, 완전탐색 아이디어 검토 후 고려
2. 재귀함수로 비효율적인 완전탐색 코드 작성후, 반복 발견. DP로 코드 개선
'''





