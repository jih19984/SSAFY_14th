# 문제
"""
start: 21:00
end: 22:00

톱니바퀴
- N극과 S극 중 하나를 나타내고 있다.
- 톱니바퀴는 번호가 매겨져 있다.
- 톱니바퀴를 회전시키려면, 회전시킬 톱니바퀴와, 방향을 결정해야 한다.
- 톱니바퀴가 회전할 때, 서로 맞닿은 극에 따라 옆에 있는 톱니바퀴를 회전시킬 수도 있고,
회전시키지 않을 수도 있다.
- 극이 같으면 회전하지 않는다!
- 극이 다르다면 회전하는 방향의 반대
- 반드시 회전하는 톱니바퀴를 기준점으로 봐야 한다!

<input>
- 첫째줄에 각 톱니바퀴의 상태가 주어진다.
    - 각 톱니바퀴의 상태는 12시부터 차례대로 읽는다. (S:1, N:0)
- 회전횟수 K가 주어진다. (1 <= K <= 100)
- K개의 줄에 걸쳐 회전시킨 방법이 주어짐. (회전시킨 톱니바퀴의 번호, 방향)
    1: 시계 방향, -1: 시계 반대 방향

<output>
K번 회전시킨 후 네 톱니바쿠의 점수의 합을 출력해라.
12시 방향이 N극이면 0점, S극이면 1점.
"""

import sys
from collections import deque
input = sys.stdin.readline

wheels = [deque(input().strip()) for _ in range(4)]
K = int(input())

def rotate_wheels(start_num, start_dir):
    rotations = [0] * 4  # 각 바퀴의 회전 방향
    rotations[start_num] = start_dir
    
    for i in range(start_num - 1, -1, -1):
        if wheels[i][2] != wheels[i+1][6]:
            rotations[i] = -rotations[i+1]
        else:
            break  # 같으면 더 이상 전파 안됨
    
    for i in range(start_num + 1, 4):
        if wheels[i-1][2] != wheels[i][6]:
            rotations[i] = -rotations[i-1]
        else:
            break 
    
    # 모든 바퀴를 동시에 회전
    for i in range(4):
        if rotations[i] != 0:
            wheels[i].rotate(rotations[i])

for _ in range(K):
    wheel_num, direction = map(int, input().split())
    rotate_wheels(wheel_num - 1, direction)

# 점수 계산
score = 0
for i in range(4):
    if wheels[i][0] == '1':  # 12시 방향이 S극
        score += 2 ** i

print(score)