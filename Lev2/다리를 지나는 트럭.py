from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge= deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    bridgeWeight = 0
    
    while(len(truck_weights)!=0):
        bridgeWeight-=bridge[-1]
        bridge.pop()
        if bridgeWeight+truck_weights[0] <= weight:
            bridge.appendleft(truck_weights.popleft())
        else:
            bridge.appendleft(0)
        bridgeWeight+=bridge[0]
        answer+=1
    return answer+bridge_length
