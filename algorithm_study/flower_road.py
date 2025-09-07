# 문제
"""
꽃밭: N x N
씨앗을 심을 수 있는 곳: (1, 1) ~ (N, N)

조건
- 꽃잎 또는 꽃술과 닿으면 안된다.
- 꽃 하나당 공간 5만큼 차지
- 이때 꽃은 최소 비용으로 공간을 차지해야 한다.
- 꽃을 3개를 채우자

입력
- 화단의 한 변의 길이: N
- 꽃밭(지점당 가격)
"""

# 풀이 방법
"""
1. 완전탐색 - 기본 탐색
- 모서리를 제외한 N-2의 크기만 검사
- 탐색한 구역 visited 방문 체크
- dfs로 모든 판을 검사하면서 최소값 갱신
- 백트래킹 없이 해보자 -> Good

1) 주변 값들의 좌표 구하기, 좌표의 value 주변의 값들 모두 더하기
2) 좌표가 범위 안넘어가는지
3) visited 상태 바꾸기
4) 현재 좌표에서 다음 좌표로 넘어갈지 / 주변의 좌표를 더할지 둘 중 하나 선택
"""

""" No Backtracking """
import sys

# (r, c)와 주변의 값들의 좌표 구하기
def cells(r, c):
    return [(r+dr, c+dc) for dr, dc in dirs]

# (r, c)의 주변의 좌표가 법위를 안넘어가는지 판별
def can_place(r, c) -> bool:
    for nr, nc in cells(r, c):
        if nr < 0 or nr >= N or nc < 0 or nc >= N:
            return False
        if visited[nr][nc]:
            return False
    return True

# (r, c)와 (r,c)의 주변 값들을 visited에서 flag(True/Flase) 변환
def place(r, c, flag) -> None:
    for nr, nc in cells(r, c):
        visited[nr][nc] = flag

# (r, c)와 (r, c) 주변의 값들의 합 계산
def cost(r, c) -> list:
    return sum(board[nr][nc] for nr, nc in cells(r, c))


def dfs(idx, count, total):
    if count == 3: # 종료 조건: 3개의 꽃을 채웠을 때 최소값 갱신
        result[0] = min(result[0], total)
        return
    
    if idx == len(centers): # 마지막 좌표를 넘어갔을 때 return
        return
    
    # center 주변 검사하지 않고 다음 인덱스 넘어가기
    dfs(idx+1, count, total)

    r, c = centers[idx]

    # center 주변 검사하고 다음 인덱스 넘어가기
    if can_place(r, c):
        place(r, c, True)
        dfs(idx+1, count+1, total + cost(r,c))
        place(r, c, False)


input = sys.stdin.readline
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False] * N for _ in range(N)]
centers = [(r,c) for r in range(1, N-1) for c in range(1, N-1)]
dirs = [(0,0), (1,0), (-1,0), (0,1), (0,-1)]
result = [float('inf')]

dfs(0, 0, 0)
print(result[0])