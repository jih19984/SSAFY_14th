# 문제
"""
자연수 N과 M이 주어졌을 때 아래 조건을 만족하는 길이가 M인 수열을 모두 구하시오.

- 1부터 N까지 자연수 중에서 중복없이 M개를 고른 수열
- 고른 수열은 오름차순이어야 한다.

1 <= M <= N <= 8

<output>
한 줄에 하나씩 문제의 조건을 만족하는 수열을 출력
"""

import sys
input = sys.stdin.readline

"""
seq 리스트의 원소를 하나씩 골라 길이가 M이되면 출력하도록
dfs 함수 작성
"""
def dfs(cnt, idx):
    global M
    if cnt == M:
        print(*result)
        return
    
    for i in range(idx, N+1):
        if not visited[i]:
            result.append(i)
            visited[i] = 1
            dfs(cnt+1, i+1)           
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())

# 1 ~ N까지 자연수를 원소로 갖는 리스트 생성
visited = [0] * (N+1)
result = []

dfs(0, 1)