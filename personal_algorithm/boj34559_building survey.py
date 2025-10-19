# 문제
"""
N x M 크기의 지도가 있다
가장 왼쪽 위 (1,1), 오른쪽 아래는 (N, M)

건물에 속하는 칸
-> 1: 건물
-> 0으로 표현된 칸 중에서 상하좌우 인접한 0으로 이동해 지도의 테두리에 도달할 수 없는 칸

관우가 임의의 두 좌표로 만들어지는 직사각형 모양의 범위에 새 건물을 지을 수 있는지 물어보았다.

새 건물을 짓기 위해서 직사각형에 포함되는 모든 칸에 건물이 포함되지 않아야 한다.

<Output>

새 건물을 지을 수 있는지 출력하시오. (YES or No)
또한 건물을 지을 수 없는 칸이 몇 칸 포함되었는지 출력하시오.

시간 및 범위
- 시간제한: 1초 (3천만 횟수)
- 1 <= N, M <= 1000
- 1 <= Q(고객의 수) <= 1e6 (백만)

-> 100만번 시행해야하므로, 무조건 규칙을 찾아야한다!
"""

# 풀이 방법
""" 
이 문제는 먼저 2가지로 단계를 나누어서 풀어야 한다.

1단계: 건물이 지어질 수 있는 곳 찾기
- 네 방향에 대해 일직선으로 이동해서 맨 끝좌표까지 가는지 확인
- c = M-1, c = 0, r = N-1, r = 0
- 좌표(base-0)는 (0,0) 과 (N-1, M-1)은 검사 제외
- 주변에 모두 1로 둘러싸인 부분 검사? 무조건 터짐

따라서 테두리에서 bfs를 돌려 방문 배열 생성
-> 하나의 테두리 시작점에서 시작하면 해당 테두리가 애초에 갇혀있으면 bfs가 돌다가 끝나버림
-> 따라서 모든 테두리의 위치에서 bfs를 돌려 방문처리를 한다.
-> 이후 방문하지 않은 곳은 건물이 지어질 수 있는 곳이므로 1을 할당한다.
-> 테두리에 건물이 있을 수 있음에 유의

2단계: 누적합을 이용한 dp배열 생성
맨날 쓰던 누적합 공식 그대로 쓰면 된다!
"""

import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(input().strip()) for _ in range(N)]
visited = [[0] * M for _ in range(N)]

# 테두리의 모든 좌표를 bfs에 돌리기 위해 한 곳에 모은다.
# 알고보니 테두리 중에 한 곳에서만 돌리면 된다...

edge = [(0,0)]
            
# edge 확인
# print(edge_lst)

# 1단계 BFS
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]

queue = deque(edge)

while queue:
    r, c = queue.popleft()
    visited[r][c] = 1
    for dr, dc in zip(dir_r, dir_c):
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and arr[nr][nc] != '1':
                visited[nr][nc] = 1
                queue.append((nr, nc))

# visited 배열 체크
# for che in visited:
#     print(*che)


# visited 배열의 값이 0이고 arr의 값이 0인 곳에 건물을 채운다
for r in range(N):
    for c in range(M):
        if arr[r][c] == '0' and visited[r][c] == 0:
            arr[r][c] = '1'

# arr check
# for r in range(N):
#     print(arr[r])

# 2단계
# 먼저 각 dp 배열에 (0,0) 부터 (r,c)까지 사각형 넓이를 저장
# 우리가 구해야할 건 건물을 지을 수 없는 칸이 몇칸인가
# 즉 arr의 1을 세야함.

dp = [[0] * (M + 1) for _ in range(N + 1)]

for r in range(1, N + 1):
    for c in range(1, M + 1):
        if arr[r-1][c-1] == '1':
            building = 1  
        else:
            building = 0
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + building

Q = int(input())

for _ in range(Q):
    r1, c1, r2, c2 = map(int, input().split())
    
    # 누적합으로 직사각형 내 건물 개수 계산
    result = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    
    if result == 0:
        print("Yes")
    else:
        print(f"No {result}")

                
            


