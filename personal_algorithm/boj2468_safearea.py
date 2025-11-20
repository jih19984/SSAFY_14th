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

""" 함수 정의"""
def bfs(start_r, start_c, visited, high):
    queue = deque([(start_r, start_c)])
    
    while queue:
        st_r, st_c = queue.popleft()
        for dr, dc in zip(dir_r, dir_c):
            nr = st_r + dr
            nc = st_c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc] and arr[nr][nc] > high:
                    visited[nr][nc] = True
                    queue.append((nr, nc))

""" 변수 및 객체 정의 """
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
high_set = []
dir_r = [1, 0, -1, 0]
dir_c = [0, 1, 0, -1]
max_safe_area_count = 0

""" 배열을 리스트로 묶어서 set로 변환 """
for idx in range(N):
    high_set.extend(arr[idx])
    
high_set = set(high_set)

# 주의사항: 문제의 노트에 아무지역도 물에 잠기지 않을 수 있다고 적혀있음
# high_set에 0을 추가해 어떤 지역도 잠기지 않는 것도 고려해야 함.
high_set.add(0)

""" 높이 별로 안전한 영역 개수 계산"""
for high in high_set:
    visited = [[False] * N for _ in range(N)]
    safe_area_count = 0
    for r in range(N):
        for c in range(N):
            if arr[r][c] > high and not visited[r][c]:
                visited[r][c] = True
                bfs(r, c, visited, high)
                safe_area_count += 1

    max_safe_area_count = max(safe_area_count, max_safe_area_count)
    
""" 결과 출력 """
print(max_safe_area_count)