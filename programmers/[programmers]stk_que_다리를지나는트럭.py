from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge_weight = 0    
    bridge_queue  = deque([0]*bridge_length)
    truck_queue   = deque(truck_weights)
    
    while truck_queue:
        tp = truck_queue.popleft()
        while True:
            bridge_weight -= bridge_queue.popleft()
            time += 1
            if bridge_weight + tp > weight:
                bridge_queue.append(0)
            else:
                bridge_queue.append(tp)
                bridge_weight += tp
                break
    
    return time + bridge_length
