import sys
if __name__ == "__main__":
    N = int(sys.stdin.readline())
    words = [sys.stdin.readline().rstrip() for _ in range(N)]
    words = set(words)
    words = list(words)
    words.sort(key=lambda x: (len(x),x))
    for w in words:
        print(w)