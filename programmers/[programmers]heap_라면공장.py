import heapq

def solution(stock, dates, supplies, k):
    answer, front = 0, 0
    h = []
    holdday = stock - 1
    
    while holdday < k - 1 :
        for i in range(front, len(dates)):
            if dates[i] <= holdday + 1:
                heapq.heappush(h, -supplies[i])
            else:
                front = i
                break
        holdday -= heapq.heappop(h)
        answer += 1
        
    return answer
