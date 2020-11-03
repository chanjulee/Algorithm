'''
def solution(scoville, K):
    answer = 0
    scoville.sort()
    while True:
        if scoville[0]>=K:
            break
        if len(scoville)<2:
            return -1
        temp = scoville.pop(0)+scoville.pop(0)*2
        scoville.append(temp)
        scoville.sort()
        answer +=1
    return answer
'''
import heapq
def solution(scoville, K):
    answer = 0
    heap = []
    for x in scoville:
        heapq.heappush(heap,x)

    while True:
        if heap[0]>=K: 
            break
        if len(heap)<2:
            return -1
        temp = heapq.heappop(heap)+heapq.heappop(heap)*2
        heapq.heappush(heap, temp)
        answer +=1

    return answer


scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))