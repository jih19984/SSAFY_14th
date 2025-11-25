from collections import deque

def solution(maps):
    def bfs(st_r, st_c, check_arr, arr):
        nonlocal N, M
        queue = deque([(st_r,st_c)])
        check_arr[st_r][st_c] = True
        area_sum = int(list(arr[st_r])[st_c])
        while queue:
            st_r, st_c = queue.popleft()
            for dr, dc in zip(dir_r, dir_c):
                nr, nc = st_r + dr, st_c + dc
                if 0 <= nr < N and 0 <= nc < M:
                    if list(arr[nr])[nc] != 'X':
                        if not check_arr[nr][nc]:
                            check_arr[nr][nc] = True
                            queue.append((nr, nc))
                            area_sum += int(list(arr[nr])[nc])
        return area_sum
    
    # 맵의 길이
    answer = []
    N = len(maps) # 세로 길이
    M = len(maps[0]) # 가로 길이
    dir_r = [1, 0, -1, 0]
    dir_c = [0, 1, 0, -1]
    visited = [
     [False] * M for _ in range(N)
    ]
    
    for r in range(N):
        row = list(maps[r])
        for c in range(M):
            if row[c] != "X" and not visited[r][c]:
                print(r, c)
                sum_ele = bfs(r, c, visited, maps)
                answer.append(sum_ele)
    
    if answer == []:
        return [-1]
    
    answer.sort()
    return answer