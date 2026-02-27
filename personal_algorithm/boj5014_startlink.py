# 문제
"""
총 층수: F
스타트링크가 있는 곳의 위치: G
강호의 위치: S

엘리베이터를 타고 G층으로 이동하려고 한다.

엘리베이터
- U: 위로 가는 버튼
- D: 아래로 가는 버튼

강호가 G층에 도착하기 위해 버튼을 최소 몇 번 눌러야 하는가?

<입력>
F, S, G, U, D

<출력>
최소값 출력.
이동할 수 없을 때는 "use the stairs"를 출력
"""

"""입력"""
from collections import deque
import sys
input = sys.stdin.readline
F, S, G, U, D = map(int, input().split())

"""메인"""
def bfs():
    # visited[i]는 방문여부만 체크하는 게 아님! 이동횟수도 저장
    visited = [-1] * (F + 1)
    queue = deque([S])
    visited[S] = 0 # 시작 층 방문 처리

    while queue:
        curr = queue.popleft()

        # 목표 층에 도착
        if curr == G:
            return visited[curr]
            
        # 위(U) 혹은 아래(D)
        for next_floor in (curr + U, curr - D):
            # 1. 건물 범위 내에 있고 2. 아직 방문하지 않았다면
            if 1 <= next_floor <= F and visited[next_floor] == -1:
                visited[next_floor] = visited[curr] + 1
                queue.append(next_floor)

    return "use the stairs"

"""출력"""
print(bfs())