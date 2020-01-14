from itertools import permutations

# return score
def score(Anums, Bnums):
    s = 0
    b = 0

    Anums = str(Anums)
    Bnums = str(Bnums)
    for i in range(3):
        if Anums[i] == Bnums[i]:
            s += 1
        else:
            for j in range(3):
                if Anums[i] == Bnums[j]:
                    b += 1
    
    return s, b


def solution(baseball):
    digit = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    num_list = list(permutations(digit, 3))

    nums = []
    for itm in num_list:
        nums.append(itm[0] * 100 + itm[1] * 10 + itm[2])

    # set 0 impossible answer
    for itm in baseball:
        for j in range(len(nums)):
            if nums[j]:
                s, b = score(itm[0], nums[j])
                if (itm[1]!=s) or (itm[2]!=b):
                    nums[j] = 0

    # count possible answer
    answer = 0
    for itm in nums:
        if itm:
            answer += 1
    return answer
