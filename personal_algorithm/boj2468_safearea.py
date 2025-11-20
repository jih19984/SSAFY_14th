# 문제
"""
물에 잠기지 않는 최대 안전 영역의 개수를 구하시오.
"""

# 풀이
"""
높이는 1~100 사이

1. 모든 높이를 볼 필요가 없으므로, 집합으로 중복된 높이는 제거
2. 높이 정보보다 높은 arr를 기준으로 bfs를 돌리며 safe_area count
3. max함수로 safe_area count 갱신
"""
from collections import deque
import sys
input = sys.stdin.readline

def bfs(start_r, start_c, visited, rain_level):
    queue = deque([(start_r, start_c)])
    visited[start_r][start_c] = True
    
    while queue:
        r, c = queue.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if arr[nr][nc] > rain_level and not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
        
    

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
high_lst = []
dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]

for i in range(N):
    high_lst.extend(arr[i])
    
high_lst = set(high_lst)
high_lst.add(0)

max_safe_areas = 0

for rain_level in high_lst:
    visited = [[False] * N for _ in range(N)]
    safe_area_count = 0
    
    for r in range(N):
        for c in range(N):
            if arr[r][c] > rain_level and not visited[r][c]:
                bfs(r, c, visited, rain_level)
                safe_area_count += 1
                
    max_safe_areas = max(max_safe_areas, safe_area_count)
    

print(max_safe_areas)
    
    