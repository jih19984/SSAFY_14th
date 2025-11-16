# 문제
"""
돌을 이용해 재밌는 게임을 하려고 한다.
돌은 세개의 그룹으로 나뉘어져 있으며, 각각의 그룹에는 돌이 A, B, C개가 있다.

모든 그룹에 있는 돌의 개수를 같게 만들고자 한다.

돌은 단계별로 움직인다.

1. 크기가 같지 않은 두 그룹을 고른다.
돌의 개수가 작은 쪽: X
돌의 개수가 많은 쪽: Y

2. 돌의 개수 더하기
X에 있는 돌의 개수: X + X
Y에 있는 돌의 개수: Y - X

A, B, C가 주어졌을 때 돌을 같은 개수로 만들 수 있으면 1, 아니면 0을 출력하시오.

1 <= A, B, C <= 500
"""

# 풀이
"""
음... 계속해서 돌을 2그룹으로 선택해서 세 개의 돌이 같은지 체크? -> bfs
"""

import sys
from collections import deque

input = sys.stdin.readline

A, B, C = map(int, input().split())

# 총합이 3으로 나누어 떨어지지 않으면 불가능
total = A + B + C

if total % 3 != 0:
    print(0)
    exit()

target = total // 3

# BFS
visited = set()
queue = deque([(A, B, C)])
visited.add([A, B, C])

def get_next_states(a, b, c):
    """현재 상태에서 가능한 다음 상태들"""
    states = []
    groups = [a, b, c]

    # 3개 그룹 중 2개 선택 (3C2 = 3)
    for i in range(3):
        for j in range(i+1, 3):
            if groups[i] != groups[j]:
                x = min(groups[i], groups[j])
                y = max(groups[i], groups[j])

                # 새로운 상태
                new_groups = groups[:]
                new_groups[i] = x + x
                new_groups[j] = y - x

                # 정렬해서 중복 방지
                new_state = tuple(sorted(new_groups))
                states.append(new_state)

    return states

while queue:
    current = queue.popleft()
    a, b, c = current

    # 목표 달성
    if a == b == c == target:
        print(1)
        exit()

    for next_state in get_next_states(a, b, c):
        if next_state not in visited:
            visited.add(next_state)
            queue.append(next_state)

print(0)
