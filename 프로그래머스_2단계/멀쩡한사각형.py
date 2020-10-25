from math import gcd
def solution(w,h):
    #최대공약수로 나눠서 젤작은단위?부분(서로소)을 구해
    numGcd = gcd(w,h)
    w2 = w/numGcd
    h2 = h/numGcd
    #서로소에서 제거된 사각형수
    temp2 = 1+w2-1+h2-1
    answer = w*h - numGcd*temp2
    return answer