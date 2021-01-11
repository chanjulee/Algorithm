import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    data = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
    data.sort(key=lambda x: (x[1],x[0])) #4 4 랑 3 4 생각하면, x[0] 정렬도 해줘야함.
    
    count = 1 #첫번째 회의
    temp = data[0]
    for x in data[1:]: #꼭 잘라줘야 첫번째회의가 1 1 인경우, OK
        if x[0]<temp[1]:
            continue
        else:
            temp = x
            count += 1
    print(count)

'''import sys
sys.stdin = open("input.txt","rt")
N = int(sys.stdin.readline())

meetings = []
for i in range(N):
    start, end = map(int,sys.stdin.readline().split())
    meetings.append((start, end, end-start))

meetingsSorted = sorted(meetings, key=lambda x:(x[1],x[0]))
print(meetingsSorted)

temp = 0 #기준 시간
count = 0 #회의 카운트
for i in meetingsSorted:
    if count == 0 : #첫 회의
        temp = i[1]
        count += 1
        #print(i)
    elif count!=0 and i[0]>=temp: #다음 회의
        temp = i[1]
        count += 1
        #print(i)

print(count)
        '''
        