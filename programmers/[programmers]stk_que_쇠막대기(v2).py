def solution(arrangement):
    answer = 0
    sticks = 0
    
    for i in arrangement.replace('()', '0'):
        # laser
        if i == '0':
            answer += sticks
        # stick start
        elif i=='(':
            sticks += 1
            answer += 1
        # stick end
        else:
            sticks -= 1
            
    return answer
