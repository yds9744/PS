def solution(prices):
    answer = [0] * len(prices)
    stk = []
    last_idx = len(prices)-1
    
    for i, v in enumerate(prices):
        while stk and v < stk[-1][1]:
            pi, pv = stk.pop()
            answer[pi] = i - pi
        stk.append([i, v])
    
    while stk:
        pi, pv = stk.pop()
        answer[pi] = last_idx - pi
        
    return answer
