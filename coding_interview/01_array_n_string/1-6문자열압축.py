def solution(string):
    new_string = ""
    cur_char = ''
    cnt = 0
    
    # build string
    for i in string:
        if i==cur_char: cnt+=1
        else:
            new_string += cur_char + str(cnt)
            cur_char = i
            cnt = 1
    new_string += cur_char + str(cnt)

    # return shorter one
    if len(string) < len(new_string[1:]): return string
    else: return new_string[1:]

print(solution('aabcccccaaa'))
