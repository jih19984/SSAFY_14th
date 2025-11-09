# 문제
"""
start: 03:50 
end: 5:40

제일 왼쪽 위에서 출발하여 제일 오른쪽 아래 지점까지 항상 내리막길로 이동하는
경로의 개수를 구하시오.

N과 M은 500이하의 자연수
"""

# 풀이 방법
"""
1. 처음 시작점의 높이를 큐에 넣기
2. 자기보다 작은 높이의 좌표 모두 큐에 넣기 (4방향))
3. 마지막 점에 도착했는지 어떻게 판별할 것인가? 마지막 칸에 도달할 때마다 경로 +1
-> 18%에서 시간 초과

-> memoization 즉 중복된 경로를 한 번 더 계산하는 것을 막아야 한다.
-> bfs X, dfs X -> dp?
-> 어떻게 중복된 경로를 막을 것인가?
-> 출발점이 시작이 아닌 가장 큰 수를 기준으로 dp 순회  
"""

# 단순 BFS
"""
import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    global total_cnt    
    queue = deque([(0, 0)])

    while queue:
        r, c = queue.popleft()
        if r == R-1 and c == C-1:
            total_cnt += 1
            continue
        for dr, dc in zip(dir_r, dir_c):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[r][c] > arr[nr][nc]:
                    queue.append((nr, nc))

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
total_cnt = 0
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
bfs()
print(total_cnt)
"""

import sys
from collections import deque
input = sys.stdin.readline

def solve():
    dp[0][0] = 1
    positions = []
    for r in range(R):
        for c in range(C):
            positions.append((arr[r][c], r, c))
    
    positions.sort(reverse=True)
    
    for height, r, c in positions:
        if dp[r][c] == 0:
            continue
            
        for dr, dc in zip(dir_r, dir_c):
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[r][c] > arr[nr][nc]:
                    dp[nr][nc] += dp[r][c]
    return

R, C = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(R)]
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
dp = [[0] * C for _ in range(R)]
solve()
print(dp[R-1][C-1])