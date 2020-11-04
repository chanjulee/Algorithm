N = 7

title = 666 #제일 처음 타이틀
while N:
    if '666' in str(title):
        N-=1 #666이 들어갈때마다 N줄여줌
    title+=1 #1씩 늘려감
print(title-1) #마지막에 1더한거 빼주고 출력
