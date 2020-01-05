# programmers_stk&que_printer
# queue problem
# jinsun

from collections import deque

def solution(priorities, location):
    answer = [0]*len(priorities)
    cnt = 1

    que = deque([])
    for i, p in enumerate(priorities):
        que.append([i, p])
        
    for i in range(9, 0, -1):
        tmpque = deque([])
        n = len(que)
        for j in range(n):
            p = que.popleft()
            if i == p[1]:
                answer[p[0]] = cnt
                cnt += 1
                que.extend(tmpque)
                tmpque = deque([])
            else:
                tmpque.append(p)
        tmpque.extend(que)
        que = deque(tmpque)
        
    return answer[location]
