def solution(s):
    numbers = s.split(' ')
    numbers = list(map(int, numbers))
    numbers.sort()
    return str(numbers[0])+" "+str(numbers[len(numbers)-1])

s = "-1 -2 -3 -4"
print(solution(s))