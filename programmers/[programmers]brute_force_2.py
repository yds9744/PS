def solution(numbers):

    # count numbers
    number = [0] * 10
    for i in numbers:
        number[int(i)] += 1

    # make prime list
    maxn = 10 ** len(numbers)
    prime = [True] * maxn
    prime[0] = False
    prime[1] = False
    for i in range(2, maxn):
        if prime[i]:
            for j in range(i*2, maxn, i):
                prime[j] = False

    # check whether prime exists
    answer = 0
    for pnum in range(len(prime)):
        if prime[pnum]:
            answer += 1
            cnumber = number[:]
            for i in str(pnum):
                if cnumber[int(i)]:
                    cnumber[int(i)] -= 1
                else:
                    answer -= 1
                    break
    
    return answer
