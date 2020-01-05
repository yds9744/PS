# programmers_queue <develope>
# jinsun

from math import ceil
from collections import deque

def solution(progresses, speeds):
    answer = []

    # make complete_day
    complete_day = deque([])
    for i, j in zip(progresses, speeds):
        complete_day.append(ceil((100-i)/j)) 

    # queue
    cur_fst = complete_day[0]
    cur_cnt = 0
    while complete_day:
        p = complete_day.popleft()
        if cur_fst >= p:
            cur_cnt += 1
        else:
            answer.append(cur_cnt)
            cur_fst = p
            cur_cnt = 1
    answer.append(cur_cnt)
    
    return answer
