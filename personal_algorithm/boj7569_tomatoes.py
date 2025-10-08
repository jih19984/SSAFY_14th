# 문제
"""
토마토는 상하좌우, 그리고 같은 층의 위 아래에 영향을 준다.
H층의 가로 M 세로 N의 상자안의 토마토 정보가 주어질 때,
모든 토마토가 익으려면 며칠이 걸리는가?

2 <= M <= 100
2 <= N <= 100
1 <= H <= 100

만약 토마토가 모두 익지 못한다면 -1을 출력.
원래부터 토마토가 익어있어다면 0을 출력 
"""

# 풀이 방법
"""
층별로 탐색을 위해 3차원적으로 생각해야 한다
토마토의 출발 위치에서 모두가 동일하게 퍼져야 한다는 점을 고려할 때 BFS가 가장 적합하다!
"""

import sys
from collections import deque
input = sys.stdin.readline

M, N, H = map(int, input().split())

arrs = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

# 3차원 배열 체크
# for arr in arrs:
#     print(arr)
tomato_loc = []

# 상하좌우 위 아래 방향 (h,r,c)
dirs = [(0,0,1), (0,1,0), (0,0,-1), (0,-1,0), (1,0,0), (-1,0,0)]
check = 0

"""
토마토는 반드시 한 개 이상 있음에 유의
토마토 배열에 0이 없다면: 0 출력
토마토가 모두 익지 못하는 상황: -1 출력
"""
# 토마토가 있는 위치 찾아서 층수를 인덱스로 (r,c) 저장
for h in range(H):
    for r in range(N):
        for c in range(M):
            if arrs[h][r][c] == 1:
                tomato_loc.append((h, r, c))
            elif arrs[h][r][c] == 0:
                check = 1

queue = deque()
day = 0
max_day = 0

for tomato in tomato_loc:
    h, r, c = tomato
    queue.append([h, r, c, day])

# 토마토의 초기 위치에서부터 모두 bfs로 퍼뜨림.
# 이 때 토마토들의 초기 위치에서 동시에 퍼져야 한다.
# 일단 초기 시작점을 기준으로 퍼뜨림

# 0이 하나도 없는 경우 0  -> 최소 토마토 1개가 있기 때문에 bfs 돌릴 필요 없음. 0 출력 
# sys.exit vs SystemExit
"""
sys.exit() 자체가 내부적으로 raise SystemExit를 호출한다.
Systemexit 예외를 발생시켜 현재 스레드에서 종료 유도

raise: 예외를 직접 발생시키는 키워드
다중 for문에서 탈출시킬 때 편리
"""
if check == 0:
    print(0)
    raise SystemExit
else:
    while queue:
        h, r, c, day = queue.popleft()
        for dh, dr, dc in dirs:
            nh, nr, nc = h + dh, r + dr, c + dc
            if 0<= nh < H and 0<= nr < N and 0 <= nc < M:
                if arrs[nh][nr][nc] == 0:
                    arrs[nh][nr][nc] = 1
                    queue.append([nh, nr, nc, day + 1])
                    if day + 1 > max_day:
                        max_day = day + 1

for h in range(H):
    for r in range(N):
        for c in range(M):
            if arrs[h][r][c] == 0:
                print(-1)
                raise SystemExit
            
print(max_day)

