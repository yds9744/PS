def solution(record):
    answer = []
    dic = {}
    
    for i in range(len(record)):
        record[i] = record[i].split(" ")
        if record[i][0] != "Leave":
            dic[record[i][1]] = record[i][2]

    for r in record:
        if r[0] == "Change": continue
        elif r[0] == "Enter":
            answer.append(dic[r[1]] + "님이 들어왔습니다.")
        else:
            answer.append(dic[r[1]] + "님이 나갔습니다.")
    
    return answer
