import sys
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
        
        