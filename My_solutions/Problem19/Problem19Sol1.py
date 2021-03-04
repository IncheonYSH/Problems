from collections import deque
def solution(bridge_length, weight, truck_weights):
    answer = 0
    now_weight = 0
    truck_weights = deque(truck_weights)
    on_bridge = deque([0])
    on_location = deque([1])
    
    while len(on_location) > 0:
        answer += 1
        for i in range(len(on_location)):
            on_location[i] = on_location[i] - 1
        if on_location[0] == 0:
            on_location.popleft()
            truck_end = on_bridge.popleft()
            now_weight -= truck_end
        else:
            pass
        
        if len(truck_weights) == 0:
            continue
        elif now_weight + truck_weights[0] <= weight:
            truck_start = truck_weights.popleft()
            on_bridge.append(truck_start)
            on_location.append(bridge_length)
            now_weight += truck_start
        else:
            continue
    
    return answer