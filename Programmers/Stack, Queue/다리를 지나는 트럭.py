from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    wait = deque()
    bridge = deque()
    empty = deque([0] * len(bridge_length))
    t_pass = []
    for i in truck_weights:
        wait.append(i)

    while len(t_pass) != len(truck_weights):
        if not wait:
            t_pass.append(bridge.popleft())
            time += 1
            continue
        truck = wait.popleft() # 트럭을 넣고
        bridge.append(truck) # 다리에 트럭한대 입장
        time += 1 # 시간은 증가

        if sum(bridge) > weight or len(bridge) > bridge_length: # 만약 트럭 전체무게가 더 무겁다면
            wait.appendleft(truck) # 들어온 트럭은 다시 빠지고
            t_pass.append(bridge.popleft()) # 원래있던 트럭은 지나간다

    
    

    
    return time