#알리바바와 40인의 도둑(Top-Down)
import sys
n = int(sys.stdin.readline())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
dp = [[0]*n for _ in range(n)]
