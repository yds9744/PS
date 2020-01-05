def solution(arrangement):
    cur_iron = 0
    laser = False
    stk = []
    answer = 0
    
    for i, j in zip(arrangement, arrangement[1:]+'0'):
        # laser ')'
        if laser:
            laser = False
            continue
        # laser '('
        if i+j == '()':
            laser = True
            answer += cur_iron
        # iron '('
        elif i=='(':
            stk.append(0)
            cur_iron += 1
            answer += 1
        # iron ')'
        else:
            stk.pop()
            cur_iron -= 1
            
    return answer
