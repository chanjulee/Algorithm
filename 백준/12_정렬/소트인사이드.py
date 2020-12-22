import sys
if __name__ == "__main__":
    nums = list(sys.stdin.readline())
    nums.sort(reverse=True)
    for n in nums:
        print(n, end='')