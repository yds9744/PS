import heapq

def solution(operations):
    idx, qsize = 0, 0
    exist = []
    maxh = []
    minh = []
    
    for oper in operations:
        if oper == 'D 1' and qsize > 0:
            while not exist[maxh[0][1]]:
                heapq.heappop(maxh)
            n, i = heapq.heappop(maxh)
            exist[i] = False
            qsize -= 1
            
        elif oper == 'D -1' and qsize > 0:
            while not exist[minh[0][1]]:
                heapq.heappop(minh)
            n, i = heapq.heappop(minh)
            exist[i] = False
            qsize -= 1
            
        elif oper[:2] == 'I ':
            num = int(oper[2:])
            heapq.heappush(maxh, (-num, idx))
            heapq.heappush(minh, (num, idx))
            exist.append(True)
            idx += 1
            qsize += 1
    
    if qsize > 0:
        while not exist[maxh[0][1]]:
            heapq.heappop(maxh)
        while not exist[minh[0][1]]:
            heapq.heappop(minh)
        return [-maxh[0][0], minh[0][0]]
    else :
        return [0, 0]
