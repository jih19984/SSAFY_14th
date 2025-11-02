# 문제
"""
2차원 배열(한 덩어리의 빙산)이 주어질 때, 두 덩어리 이상으로 분리되는 최초의 시간(년)을 구하시오.

- 빈 칸은 모두 0으로 채워짐
- 빙산의 높이는 바닷물에 접해 있는 부분이 많을수록 더 빨리 줄어든다.
"""

# 풀이 방법
"""
두 덩어리로 분리되어 있는지 어떻게 확인할 것인가?
-> dfs, bfs 돌려보기 -> dfs는 깊이 제한으로 터짐.

2차원 배열을 deepcopy로 복사한 결과 시간초과 발생.
새로운 배열을 만들어서 값을 할당하는게 더 효율적
"""

import sys
from collections import deque

input = sys.stdin.readline

# input
N, M = map(int, input().split()) 
arr = [list(map(int, input().split())) for _ in range(N)]
total_cnt = 0
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]

# 2차원 배열에서 숫자찾아서 빙산 깎기
def find_ice():
    next_arr = [[0] * M for _ in range(N)]  # 새로운 배열 생성
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0:
                adj_cnt = 0
                for dr, dc in zip(dir_r, dir_c):
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                        adj_cnt += 1
                next_arr[r][c] = max(0, arr[r][c] - adj_cnt)
            else:
                next_arr[r][c] = 0
    return next_arr

# 분리되어 있는지 체크하기
def count_components():
    visited = [[False] * M for _ in range(N)]
    count = 0
    
    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited[start_r][start_c] = True
        
        while queue:
            r, c = queue.popleft()
            for dr, dc in zip(dir_r, dir_c):
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and arr[nr][nc] > 0:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    
    for r in range(N):
        for c in range(M):
            if arr[r][c] > 0 and not visited[r][c]:
                bfs(r, c)
                count += 1
    return count

# 전체 함수 실행
# find_ice를 빙산이 두 개로 분리될 때까지 시행
while True:
    components = count_components()
    if components >= 2:
        print(total_cnt)
        break
    if components == 0:  # 모든 빙산이 녹음
        print(0)
        break
    
    arr = find_ice()  # 새로운 배열 반환받기
    total_cnt += 1

