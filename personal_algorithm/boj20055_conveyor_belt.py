# 문제
"""
길이가 N인 컨베이어 벨트가 있고, 길이가 2N인 벨트가 위아래로 감싸며 돌고 있다.
벨트는 1번부터 2N번까지 칸으로 나뉘어 있으며, 각 칸에는 내구도가 있다.
로봇은 올리는 위치(1번)에서만 올릴 수 있고, 내리는 위치(N번)에 도달하면 즉시 내린다.
내구도가 0인 칸의 개수가 K개 이상이 되면 과정을 종료한다.
"""

# 풀이 방법
"""
collections.deque를 사용하여 벨트 회전(rotate)을 효율적으로 처리한다.
벨트 내구도와 로봇 존재 여부를 각각 deque로 관리한다.
문제 조건에 따라 1단계(회전), 2단계(로봇 이동), 3단계(로봇 올리기), 4단계(종료 검사)를 시뮬레이션
로봇 이동 시 가장 먼저 올라간 로봇(내리는 위치에 가까운 로봇)부터 처리해야 하므로
인덱스 N-2부터 0까지 역순으로 확인한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    # N: 컨베이어 벨트 길이 (올리는 위치 ~ 내리는 위치)
    # K: 내구도 0인 칸의 종료 기준 개수
    N, K = map(int, input().split())
    
    # 벨트의 내구도 정보
    belt = deque(map(int, input().split()))
    
    # 로봇 존재 여부 (로봇은 윗면인 0 ~ N-1 구간에만 존재 가능)
    # 여기서는 벨트와 동일하게 회전시키기 위해 N 크기의 deque를 사용 (윗면만 관리)
    robot = deque([False] * N)
    
    step = 0
    
    while True:
        step += 1
        
        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 회전한다.
        belt.rotate(1)
        robot.rotate(1)
        
        # 내리는 위치(N-1)에 있는 로봇은 즉시 내린다.
        robot[-1] = False # robot deque의 크기가 N이므로 마지막 원소가 내리는 위치
        
        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다.
        # 로봇은 N-1번(내리는 위치)에는 없으므로(위에서 내림), N-2번부터 0번까지 확인
        for i in range(N-2, -1, -1):
            # 현재 칸에 로봇이 있고, 다음 칸에 로봇이 없고, 다음 칸 내구도가 1 이상이면
            if robot[i] and not robot[i+1] and belt[i+1] > 0:
                robot[i] = False
                robot[i+1] = True
                belt[i+1] -= 1
        
        # 이동 후에도 내리는 위치에 도달한 로봇은 내림
        robot[-1] = False
        
        # 3. 올리는 위치에 있는 칸의 내구도가 0이 아니면 올리는 위치에 로봇을 올림
        if belt[0] > 0:
            robot[0] = True
            belt[0] -= 1
            
        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료
        if belt.count(0) >= K:
            break
            
    print(step)

solve()