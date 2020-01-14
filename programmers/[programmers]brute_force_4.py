import math

def solution(brown, red):
    # get factor pair
    factor = []
    for i in range(1, math.floor(red ** 0.5) + 1):
        if red % i == 0:
            factor.append([red//i + 2, i + 2])

    # (itm[0]-2) * (itm[1]-2) == red
    # itm[0]     * itm[1]     == red + brwon ? => answer!
    answer = []
    for itm in factor:
        if red + brown == itm[0] * itm[1]:
            answer = itm

    return answer
