from bisect import bisect_left, bisect_right
def count_by_range(array, left_value, right_value):
    right_index = bisect_right(array, right_value)
    left_index = bisect_left(array, left_value)
    return right_index - left_index

import sys
if __name__=="__main__":
    N = int(sys.stdin.readline())
    cards = list(map(int,sys.stdin.readline().split()))
    cards.sort()
    M = int(sys.stdin.readline())
    array = list(map(int,sys.stdin.readline().split()))
    for x in array:
        print(count_by_range(cards, x, x), end=' ')
