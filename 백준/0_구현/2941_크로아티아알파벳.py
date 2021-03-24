import sys
word = sys.stdin.readline().rstrip()

count = 0
while word:
    if word[:2] in ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=']:
        word = word[2:]
    elif word[:3] == 'dz=':
        word = word[3:]
    else:
        word = word[1:]
    count += 1

print(count)