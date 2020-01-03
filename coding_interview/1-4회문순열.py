from itertools import permutations

def solution(string):
    string = string.lower().replace(' ', '')
    perm = list(map(''.join, permutations(string)))
    for i in perm:
        if i == i[::-1]: return True
    return False

print(solution('Tact Coa'))
