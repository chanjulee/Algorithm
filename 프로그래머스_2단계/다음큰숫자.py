def solution(n):
    count1 = bin(n).count('1')
    temp = n
    while True:
        temp += 1
        if bin(temp).count('1')==count1:
            return temp
    return 0

print(solution(78))