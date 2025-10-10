# 문제
"""
백준에서 틀린 제출을 할 때마다 팔굽혀펴기를 5회 한다.

각 계란에는 내구도와 무게가 정해져있다.
계란으로 계란을 치게 되면 각 계란의 내구도는 상대 계란의 내구도만큼 깎인다.
그리고 내구도가 0이 되는 순간 깨진다.

일렬로 놓여있는 계란에 대해 왼쪽부터 차례로 계란을 치면서 최대한 많은 계란을 깨려고 한다.
- 가장 왼쪽의 계란을 든다.
- 이후 다른 계란 중 하나를 친다.
- 만약 손에 든 계란이 깨졌거나, 다른 계란이 없으면 치지 않는다.
- 그 다음 오른쪽 칸 계란을 들고 위의 과정을 반복
- 만약 가장 최근에 든 계란이 가장 오른쪽인 경우 종료한다.

일렬로 놓인 계란들의 내구도와 무게가 차례대로 주어졌을 때 최대 몇 개의 계란을 깰 수 있는가?

 1 <= N <= 8 and 1 <= s, w <= 300

<input>
계란의 수 N
N개의 줄에 걸쳐 계란의 내구도와 무게
"""

# 풀이 방법
"""
어떻게 해야 계란을 많이 깰 수 있을까?

일단 들고 있는 계란이 깨지면 백트래킹 하는 걸로 ~~ 

종료 조건: N번째 계란까지 모두 순회했을 때

가지 치기
- 기준 계란 주변에 칠 수 있는 계란이 없을 때 다음으로
- 현재 계란이 깨져있다면, 다음으로
"""

import sys

input = sys.stdin.readline

def backtrack(idx):
    global result

    # 계란을 모두 순회했을 때?
    if idx == N:
        # 깨진 계란의 개수 카운트
        cnt = sum([1 for s, w in eggs if s <= 0])
        result = max(result, cnt)
        return

    # 계란이 깨져있는 상태라면
    if eggs[idx][0] <= 0:
        backtrack(idx+1) # 다음 계란으로 pass
        return
    
    # 만약 칠 수 있는 계란이 없다면 다음으로 넘겨야 한다.
    # 왜? idx => 무조건 N에 도착하도록 종료 조건을 설정했기 때문에
    check = False
    for i in range(N):
        if i != idx and eggs[i][0] > 0:
            check = True
            break

    if not check:
        backtrack(idx + 1)
        return
    
    
    for i in range(N):
        if i != idx and eggs[i][0] > 0: 
            eggs[idx][0] -= eggs[i][1]
            eggs[i][0] -= eggs[idx][1]

            backtrack(idx+1)

            eggs[idx][0] += eggs[i][1]
            eggs[i][0] += eggs[idx][1]

N = int(input())

eggs = [list(map(int, input().split())) for _ in range(N)]
result = 0
backtrack(0)

print(f"{result}")