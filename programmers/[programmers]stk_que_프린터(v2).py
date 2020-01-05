# programmers_stk&que_printer
# queue problem
# jinsun

from collections import deque

def solution(priorities, location):
    answer = 0

    que = deque(priorities)
    priorities.sort()
    m = priorities.pop()

    while que:
        p = que.popleft()
        if p == m:
            answer += 1
            if location == 0: break
            else: location -= 1
            m = priorities.pop()
        else:
            que.append(p)
            if location == 0: location = len(que) - 1
            else: location -= 1

    return answer
