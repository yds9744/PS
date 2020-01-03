from itertools import permutations

def solution(str1, str2):
    if len(str1) == len(str2) and \
        str2 in list(map(''.join, permutations(str1))):
        return True
    else:
        return False

solution('abc', 'hi')
