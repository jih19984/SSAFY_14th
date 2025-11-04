# 문제
"""
보드 크기 4x4, 6x6, 8x8
- 흑돌과 백돌이 번갈아가며 보드에 돌을 놓음
- 최종적으로 보드에 자신의 돌이 많으면 이기는 게임

보드에 빈 곳이 없거나, 양 플레이어 모두 돌을 넣을 곳이 없으면 게임 끝
그 때 보드에 있던 돌의 개수가 많은 플레이어가 승리

<출력>
게임이 끝난 후 보드 위의 흑돌, 백돌의 개수 출력
흑돌: 1, 백돌: 2

<입력>
1. 테스트케이스 개수
2. N: 보드 한 변의 길이, M: 플레이어가 돌을 놓는 횟수
3. 좌표 c, r, rock_color
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    board = [[0] * N for _ in range(N)]
    state = black
    for _ in range(M):
        if state == black:
            pass
        else:
            pass
