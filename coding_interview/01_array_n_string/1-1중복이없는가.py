def solution(string):
    d = {}              # dict(hash)
    for i in string:
        if i in d:
            return True
        else:
            d[i] = 0
    return False
