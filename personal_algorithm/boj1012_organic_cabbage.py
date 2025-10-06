# 문제
"""
배추를 해충으로부터 보호하기 위해 흰 지렁이를 구매하였다.

흰지렁이는 인접한 다른 배추로 이동 가능하다.(상하좌우)

배추들이 몇 군데에 퍼져있는지 조사하여 총 몇마리의 지렁이가 필요한지 알 수 있다.
1: 배추가 심어져 있는 땅
0: 빈 땅

<input>
가로 길이 1<=M<=50
세로 길이 1<=N<=50
배추가 심어진 위치 개수 1<=K<=2500
그 다음 줄에 배추의 위치가 주어진다.

<output>
필요한 최소 흰지렁이 마리 수를 구하시오.
"""

# 풀이 방법
"""
1이 있는 위치에서 dfs를 돌리기
스택을 이용한 dfs 구현

파이썬은 기본적으로 재귀 깊이 제한이 1000이므로
현재 문제에서 배추가 1000개 이상 연결되어 있다면,
터질 수 밖에 없음.
"""
import sys
input = sys.stdin.readline

def dfs(i, j):
    stack = [(i, j)]
    arr[i][j] = 0
    while stack:
        x, y = stack.pop()
        for dx, dy in [(0,1), (1,0), (0,-1), (-1,0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < M and arr[nx][ny] == 1:
                arr[nx][ny] = 0
                stack.append((nx, ny))
        
T = int(input())

for _ in range(T):
    cnt = 0
    M, N, K = map(int, input().split())
    arr = [[0] * M for _ in range(N)]

    # 배추가 있는 위치에 1 넣기
    for _ in range(K):
        i, j = map(int, input().split())
        arr[j][i] = 1

    for i in range(N):
        for j in range(M):
            if arr[i][j] == 1: 
                dfs(i,j)
                cnt += 1

    print(f"{cnt}")
