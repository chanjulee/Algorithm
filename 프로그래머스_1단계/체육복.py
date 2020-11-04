def solution(n, lost, reserve):
    answer = 0
    student = [5]+[1]*n+[5] #우선 다 1([5]는 index out of 어쩌고떔에...)
    for l in lost: #잃어버림 다 -1
        student[l]-=1
    for r in reserve: #여분있음 다 +1
        student[r]+=1
    for r in reserve:
        if student[r]==2 and student[r-1]==0: #우선 앞에꺼
            student[r-1]+=1
        elif student[r]==2 and student[r-1]==1 and student[r+1]==0: #그다음 뒤에꺼
            student[r+1]=1

    answer = student.count(1)+student.count(2)
    return answer

n = 6
lost = [5,6]
reserve = [4,5]
print(solution(n,lost,reserve))