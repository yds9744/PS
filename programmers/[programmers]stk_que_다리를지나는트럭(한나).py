def solution(bridge_length, weight, truck_weights):

    answer = 0
    weightNow = 0
    passing = []
    trucks = [i for i in truck_weights]

    for i, truck in enumerate(trucks):

        if len(passing) >= bridge_length:
            p = passing.pop(0)
            weightNow -= p

        if weightNow + truck <= weight:
            passing.append(truck)
            weightNow += truck
            answer += 1

        else:
            nowLen = len(passing)
            passing.extend([0]*(bridge_length - nowLen))
            answer += (bridge_length - nowLen)
            trucks.insert(i, truck)

    nowLen = len(passing)
    if nowLen > 0:
        answer += bridge_length

    return answer
