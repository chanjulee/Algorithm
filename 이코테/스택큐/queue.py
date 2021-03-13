from collections import deque

queue = deque()
queue.append(5)
queue.append(3)
queue.popleft() #FIFO: 젤앞에꺼를 뺌

queue.reverse()