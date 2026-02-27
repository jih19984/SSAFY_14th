# 문제
"""
소요시간: 50분

- 미로는 직사각형 격자모양
- 각 칸은 이동할 수 있거나, 벽을 포함.

미로 지도를 출력하시오.
F: 앞으로 한 칸
L: 왼쪽으로 방향 전환
R: 오른쪽으로 방향 전환

<입력>
- 문자열의 길이 (0이상 50미만)
- 홍준이가 적은 문자열

<출력>
.: 이동할 수 있는 칸
#: 벽
"""

import sys
input = sys.stdin.readline 

"""입력"""
N = int(input())
Dirs = list(input().strip())

"""시뮬레이션"""
# 방향: 남, 서, 북, 동 (시계방향 순서)
# 남쪽을 보고 시작하므로 index 0 = (1, 0)
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]

curr_r, curr_c = 0, 0
curr_d = 0 # 처음엔 남쪽
visited = [(curr_r, curr_c)]

for cmd in Dirs:
    if cmd == 'F':
        curr_r += dr[curr_d]
        curr_c += dc[curr_d]
        visited.append((curr_r, curr_c))
    elif cmd == 'L':
        # 왼쪽 회전은 반시계방향
        curr_d = (curr_d - 1) % 4
    elif cmd == 'R':
        # 오른쪽 회전은 시계방향
        curr_d = (curr_d + 1) % 4

# 방문한 좌표들로부터 최소/최대 r, c 찾기
min_r = min(v[0] for v in visited)
max_r = max(v[0] for v in visited)
min_c = min(v[1] for v in visited)
max_c = max(v[1] for v in visited)

# 미로 크기 계산
rows = max_r - min_r + 1
cols = max_c - min_c + 1

# 미로 초기화 (#로 채우기)
miro = [['#'] * cols for _ in range(rows)]

# 방문한 곳을 .으로 변경
for r, c in visited:
    miro[r - min_r][c - min_c] = '.'

"""출력"""
for row in miro:
    print("".join(row))