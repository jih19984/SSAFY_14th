# 문제
"""
캠퍼스 크기 N x M
캠퍼스에서 이동 방법은 상하좌우로 이동

캠퍼스의 밖으로 이동할 수 없을 때, 캠퍼스에서 도연이가 만날 수 있는 사람의 수를 출력하시오.

0: 빈 공간
X: 벽
I: 도연이
P: 사람

"""

# 풀이방법
"""
BFS, DFS로 각각 풀어보자.
"""
import sys
sys.setrecursionlimit(10**6)
from collections import deque

""" 1. 도연이의 위치 찾기 """
def find_doyeon():
    for r in range(N):
        for c in range(M):
            if campus[r][c] == 'I':
                queue.append((r,c))
                return

""" 2. 도연이가 만날 수 있는 사람 수 카운트 """
# 1. BFS
def count_person_bfs():
    global cnt_person1
    while queue:
        st_r, st_c = queue.popleft()
        for dr, dc in zip(dir_R, dir_C):
            nr = st_r + dr
            nc = st_c + dc
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc] and campus[nr][nc] != 'X':
                    visited[nr][nc] = True
                    if campus[nr][nc] == 'P':
                        cnt_person1 += 1
                    queue.append((nr, nc))

    return cnt_person1

# 2. DFS
def count_person_dfs(st_r, st_c):
    global cnt_person2
    visited[st_r][st_c] = True
    
    for dr, dc in zip(dir_R, dir_C):
        nr = st_r + dr
        nc = st_c + dc
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and campus[nr][nc] != 'X':
                    visited[nr][nc] = True
                    if campus[nr][nc] == 'P':
                        cnt_person2 += 1
                    count_person_dfs(nr, nc)

""" main 로직 """
N, M = map(int, input().split())
campus = [list(input()) for _ in range(N)]
visited = [[False] * M for _ in range(N)]
queue = deque([])
dir_R = [0, 1, 0, -1]
dir_C = [1, 0, -1, 0]
cnt_person1 = 0
cnt_person2 = 0

find_doyeon()
# result = count_person_bfs()
st_r, st_c = queue.popleft()
count_person_dfs(st_r, st_c)
result = cnt_person2

if result == 0:
    print("TT")
else:
    print(result)
