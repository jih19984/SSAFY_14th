# 문제
"""
연구소 크기: N x M
- 빈 칸: 0, 벽: 1로 구성되어 있음
- 바이러스는 상하좌우로 인접한 빈 칸으로 모두 퍼질 수 있음
- 벽은 3개 세울 수 있음. (3개 필수)

연구소의 지도가 주어졌을 때, 얻을 수 있는 안전한 영역 크기의 최댓값은?
ex)
2 0 0 0 1 1 0   
0 0 1 0 1 2 0   
0 1 1 0 1 0 0   
0 1 0 0 0 0 0
0 0 0 0 0 1 1   
0 1 0 0 0 0 0   
0 1 0 0 0 0 0
-------------
2 1 0 0 1 1 0
1 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 1 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0
"""

# 풀이 방법
"""
벽 3개 선택해 바이러스를 퍼뜨린 후 안전 영역을 모두 계산.
어떻게 계산할 것인가?
1. 빈 칸의 좌표 중 3곳에 벽을 놓는 조합을 고려
2. 2번 위치에서 BFS로 바이러스 퍼뜨림(DFS도 상관없을 듯?)
3. 전염된 칸 수 세기
4. 전체 빈 칸 수에서 벽 3개, 전염된 칸수 빼어 안전 영역 계산
5. 모든 경우의 수를 다 돌며 최대값 갱신

3 <= N, M <= 8이기 때문에 itertools를 쓰는 것이 더 효율적
itertools는 C언어로 구성되어 경우의 수가 많지 않을 때 더 빠름
"""

import sys
from itertools import combinations
from collections import deque

input = sys.stdin.readline
N, M = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]

empty = [r * M + c for r in range(N) for c in range(M) if lab[r][c] == 0]
virus = [(r, c) for r in range(N) for c in range(M) if lab[r][c] == 2]
empty_len = len(empty)
dirs = [[1,0], [-1,0], [0,1], [0,-1]]
result = 0

for wall in combinations(empty, 3):
    walls = set(wall)
    visited = set()
    q = deque(virus)
    infected_cnt = 0
    
    # BFS
    while q:
        r, c = q.popleft()
        for dr, dc in dirs:
            nr, nc = r + dr, c + dc
            if 0<= nr < N and 0<= nc < M and lab[nr][nc] == 0:
                idx = nr * M + nc
                if idx not in walls and idx not in visited:
                    visited.add(idx)
                    infected_cnt += 1
                    q.append((nr, nc))
    
    result = max(result, empty_len - infected_cnt - 3)

print(result)