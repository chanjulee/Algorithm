array = [5,7,9,0,3,1,6,2,4,8]

def quick_sort1(array, start, end):
    if start>=end: #원소가 1개인 경우 종료
        return
    pivot = start #피벗은 첫번째 원소
    left = start+1
    right = end
    while(left<=right):
        #피벗보다 큰데이터를 찾을때까지 반복
        while(left<=end and array[left]<=array[pivot]):
            left += 1
        #피벗보다 작은데이터를 찾을때까지 반복
        while(right>start and array[right]>=array[pivot]):
            right -= 1
        if(left>right): #엇갈렸을때 작은데이터와 피벗 교체
            array[right],array[pivot] = array[pivot],array[right]
        else: #엇갈리지않았다면 작은데이터와 큰데이터 교체
            array[left],array[right] = array[right],array[left]
    #분할이후 왼쪽부분과 오른쪽부분 각각 정렬수행
    quick_sort1(array,start,right-1)
    quick_sort1(array,right+1,end)

def quick_sort2(array):
    if len(array)<=1: #원소가 1개인 경우 종료
        return array
    pivot = array[0] #피벗은 첫번째 원소
    tail = array[1:] #피벗 제외한 리스트

    left_side = [x for x in tail if x<=pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if x>pivot] #분할된 오른쪽부분

    #분할이후 왼쪽부분과 오른쪽부분에서 각각 정렬수행후,전체리스트반환
    return quick_sort2(left_side)+[pivot]+quick_sort2(right_side)

if __name__ == "__main__":
    quick_sort1(array,0,len(array)-1)
    print(array)

'''
퀵정렬(+병합정렬)
평균:O(NlogN)
최악:O(N^2)
최적:O(N)
'''