def solution(heights):
    n = len(heights)
    answer = [0] * n

    heights.reverse()
    stk = []
    for i, h in enumerate(heights):
        while stk:
            p = stk.pop()
            if p[1] < h:
                answer[p[0]] = n-i
            else:
                stk.append(p)
                break
        stk.append([n-i-1, h])

    return answer
