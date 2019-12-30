import heapq
import math

def solution(jobs):
    # sort by request time
    jobs.sort(key = lambda x : x[0])
    
    # initialize
    n = len(jobs)
    answer, front, time = 0, 0, 0
    hq = []
    
    #
    while hq or front < n:
        if not hq:
            time = jobs[front][0]
        else:
            time += heapq.heappop(hq)
            answer += time
        while front < n and jobs[front][0] <= time:
            heapq.heappush(hq, jobs[front][1])
            answer -= jobs[front][0]
            front += 1
            
    return math.floor(answer/n)
