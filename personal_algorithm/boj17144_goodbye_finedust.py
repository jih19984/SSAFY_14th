# 문제
"""
시간제한 1초, 메모리 512MB
집의 크기 RxC

- 공기청정기는 항상 1번 열에 설치되어 있다.
- 공기청정기는 2행을 차지

1초마다 아래 적힌 일이 발생
- 미세먼지 확산
    * 네방향 확산
    * 확산되는 양은 /5, 소수점은 버림
    * r, c에 남은 미세먼지는 A_rc - (A_rc/5) x 확산된 방향의 개수 
- 공기청정기 작동
    * 위쪽 공기청정기의 바람은 반시계방향으로 순환
    * 아래쪽 공기청정기의 바람은 시계방향으로 순환
    * 바람이 불면 미세먼지가 바람의 방향대로 모두 한 칸씩 이동
    * 공기청정기에서 부는 바람은 미세먼지가 없는 바람, 공기청정기로 들어간 미세먼지는 모두 정화됨
"""

# 풀이 방법
"""
공기 청정기의 위치는 -1로 표시됨
T초가 지난 후 방에 남아있는 미세먼지의 양은?
<Input>
R, C, T
Array

1단계: 확산

2단계: 정화
"""

import sys
from collections import deque

# 공기청정기의 위치 puri_locs에 추가
def find_purifier():
    for r in range(R):
        if arr[r][0] == -1:
            puri_locs.append(r)

# 초기 미세먼지의 위치를 dust_locs에 추가
def fine_dust():
    dust_locs = deque()
    for r in range(R):
        for c in range(C):
            if arr[r][c] > 0:
                dust_locs.append((r,c))
    return dust_locs

# dust_locs에 있는 미세먼지들을 한 번 확산
def bfs():
    check_arr = [[0] * C for _ in range(R)]
    dust_locs = fine_dust()

    while dust_locs:
        cnt = 0
        r, c = dust_locs.popleft()
        
        for dr, dc in zip(dir_r, dir_c):
            nr = r + dr
            nc = c + dc
            if 0 <= nr < R and 0 <= nc < C:
                if arr[nr][nc] != -1:
                    # 1/5만큼 확산
                    check_arr[nr][nc] += (arr[r][c]//5)
                    cnt += 1 # 네 방향 중 몇 번 확산되었는지

        arr[r][c] = arr[r][c] - (arr[r][c]//5) * cnt
        
    # 확산된 먼지 추가
    for r in range(R):
        for c in range(C):
            arr[r][c] += check_arr[r][c]
# 공기청정기 작동
def clean_dust():
    up_loc = puri_locs[0]
    dw_loc = puri_locs[1]
    
    # 위쪽 공기청정기 (반시계방향)
    # 1. 오른쪽으로 이동
    temp = 0
    for c in range(1, C):
        temp, arr[up_loc][c] = arr[up_loc][c], temp
    
    # 2. 위로 이동  
    for r in range(up_loc-1, -1, -1):
        temp, arr[r][C-1] = arr[r][C-1], temp
    
    # 3. 왼쪽으로 이동
    for c in range(C-2, -1, -1):
        temp, arr[0][c] = arr[0][c], temp
    
    # 4. 아래로 이동
    for r in range(1, up_loc):
        temp, arr[r][0] = arr[r][0], temp
    
    # 아래쪽 공기청정기 (시계방향)
    # 1. 오른쪽으로 이동
    temp = 0
    for c in range(1, C):
        temp, arr[dw_loc][c] = arr[dw_loc][c], temp
    
    # 2. 아래로 이동
    for r in range(dw_loc+1, R):
        temp, arr[r][C-1] = arr[r][C-1], temp
    
    # 3. 왼쪽으로 이동
    for c in range(C-2, -1, -1):
        temp, arr[R-1][c] = arr[R-1][c], temp
    
    # 4. 위로 이동
    for r in range(R-2, dw_loc, -1):
        temp, arr[r][0] = arr[r][0], temp
           

input = sys.stdin.readline

R, C, T = map(int, input().split())
dir_r = [0, 1, 0, -1]
dir_c = [1, 0, -1, 0]
arr = [list(map(int, input().split())) for _ in range(R)]
puri_locs = []

# 초기 한 번 시행
find_purifier()

for _ in range(T):
    bfs()
    clean_dust()

result = 0

for r in range(R):
    for c in range(C):
        if arr[r][c] != -1:
            result += arr[r][c]

print(result)