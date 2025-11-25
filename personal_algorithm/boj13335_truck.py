# 문제
"""
start 15:42
end

강을 가로지르는 하나의 차선으로 된 다리가 하나 있다.
이 다리를 N개의 트럭이 건너가려고 한다.

- 트럭의 순서 바꾸기 불가
- 다리 위에는 w대의 트럭만 동시에 올라가기 가능
- 다리의 길이는 w 단위 길이
- 각 트럭들은 단위시간에 단위길이만큼 이동 가능
- 다리위에 온전히 올라가지 못한 트럭의 무게는 계산시 포함하지 않는다.

다리의 길이, 다리의 최대 하중, 트럭들의 무게가 순서대로 주어졌을 때, 모든 트럭이 다리를 건너는
최단시간을 구해라.

"""

# 풀이 방법
"""
예를 들어 버스 4개가 3 2 3 4가 있을 때, 다리의 길이가 5라 가정한다면?

3 2 3 버스가 들어가고 4 버스가 들어갈 것이다.
이 때 3 2 3 버스가 들어가서 나오는데 걸리는 시간을 구하는 것이 이 문제의 핵심이다.

3번 버스는 들어갈 때 다리 길이 5만큼 이동하는데 5초가 걸릴 것이다.
그다음 뒤에 붙은 2번 버스, 3번 버스가 있으므로 이 2대의 버스가 들어오는데 3초가 걸린다.

-> 생각해보니 버스가 한 그룹이 끝나고 다음 그룹이 들어오는 것이 아니다...
"""
# from collections import deque

# n, w, L = map(int, input().split())
# trucks = list(map(int, input().split()))

# bridge = deque([0] * w)
# time = 0
# truck_idx = 0
# bridge_weight = 0

# while truck_idx < n or bridge_weight > 0:
#     time += 1
    
#     exit_truck = bridge.popleft()
#     bridge_weight -= exit_truck
    
#     if truck_idx < n and bridge_weight + trucks[truck_idx] <= L:
#         bridge.append(trucks[truck_idx])
#         bridge_weight += trucks[truck_idx]
#         truck_idx += 1
#     else:
#         bridge.append(0)

# print(time)
        
    