# 문제
"""
start: 11:08
end:

- 로봇 청소기가 있는 방: NxM
- 벽 또는 빈칸으로 이루어짐
- (0,0) ~ (N-1, M-1)

청소기 작동 방식
1. 현재 칸이 청소되지 않은 경우, 현재 칸 청소

2. 현재 칸의 주변 4칸 중 청소되지 않은 빈칸이 없는 경우,
    2.1 뒤로 1칸 후진 (방향 유지) -> 1
    2.2 바라보는 방향의 뒤쪽 칸이 후진 불가라면 작동 정지

3. 현재 칸 주변의 4칸 중 청소되지 않은 빈 칸이 있는 경우,
    3.1 반 시계 방향으로 90도 회전
    3.2 바라보는 방향을 기준으로 앞쪽 칸이 청소되지 않은 경우 한 칸 전진 -> 1

d
0: 북쪽
1: 동쪽
2: 남쪽
3: 서쪽

로봇 청소기가 작동을 시작 후 멈출 때까지 청소하는 칸의 개수를 출력하시오.
"""

import sys
input = sys.stdin.readline

# input
N, M = map(int, input().split())
st_r, st_c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
work_state = True
total_count = 0
dirs = {0: (-1, 0), 1: (0, 1), 2: (1, 0), 3: (0, -1)} # 북, 동, 남, 서
dir_r = [-1, 0, 1, 0]
dir_c = [0, 1, 0, -1]

# 현재 위치 청소
def first_clean(start_r, start_c):
    global total_count
    if arr[start_r][start_c] == 0:
        arr[start_r][start_c] = 2
        total_count += 1

# 주변 4칸 청소됐는지 확인
def is_empty(start_r, start_c):
    global d, work_state, go_back_state
    check = True

    for dr, dc in zip(dir_r, dir_c):
        nr = start_r + dr
        nc = start_c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                check = False
                break

    if check:
        new_d = (d+2)%4
        move_dr, move_dc = dirs[new_d]
        move_r, move_c = start_r + move_dr, start_c + move_dc
        if arr[move_r][move_c] != 1:
            go_back_state = True
            return (move_r, move_c)
        
        else:
            work_state = False
            return (start_r, start_c)
        
    return (start_r, start_c)
    

# 주변 4칸 청소 안된 곳 확인
def is_not_empty(start_r, start_c):
    global d
    check = True

    for dr, dc in zip(dir_r, dir_c):
        nr = start_r + dr
        nc = start_c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if arr[nr][nc] == 0:
                check = False
                break

    if not check:
        d = (d+3)%4 # 반시계방향 90도 회전
        move_dr, move_dc = dirs[d]
        move_r, move_c = start_r + move_dr, start_c + move_dc
        
        if arr[move_r][move_c] == 0:
            first_clean(move_r, move_c)
            return (move_r, move_c)

    return (start_r, start_c)
    
while work_state:
    go_back_state = False
    # 1. 현재 위치 청소
    first_clean(st_r, st_c)

    # 2. 주변 4칸 청소 완료상태 체크
    st_r, st_c = is_empty(st_r, st_c)
    if go_back_state is True:
        continue

    # 3. 주변 4칸 청소 미완료상태 체크
    st_r, st_c = is_not_empty(st_r, st_c)


print(total_count)   



