# 문제
"""
소요시간: 30분
어려웠던 점: 문제의 A가 B를 신뢰하면 B가 A를 해킹할 수 있다의 의미를 양방향 그래프로 해석.

N개의 컴퓨터가 존재.

한 번의 해킹으로 여러 개의 컴퓨터를 해킹할 수 있는
컴퓨터를 해킹하고자 한다.

컴퓨터의 신뢰 관계가 주어졌을 때 가장 많은 컴퓨터를 해킹할 수 있는
컴퓨터의 번호를 오름차순으로 출력하시오. (모든 컴퓨터를 오름차순으로 출력하라는 것이 아님)

<입력>
N, M
M개의 줄에 A, B가 주어진다.
컴퓨터의 번호는 1 ~ N

<출력>
가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 오름차순으로 출력한다.

<제약>
1 <= N <= 10,000
1 <= M <= 100,000
"""

# 풀이
import sys
from collections import deque

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    A, B = map(int, input().split())
    graph[B].append(A)

# result: 가장 많은 컴퓨터를 해킹할 수 있는 컴퓨터의 번호를 저장할 리스트
result = []
max_value = -1

# 1번 노드부터 N번 노드까지 차례대로 BFS 수행
for i in range(1, N+1):
    visited = [False] * (N+1)
    visited[i] = True
    queue = deque([i])
    cnt = 1 
    while queue:
        v = queue.popleft()
        for w in graph[v]:
            if not visited[w]:
                visited[w] = True
                queue.append(w)
                cnt += 1
    if cnt > max_value:
        max_value = cnt
        result = [i]
    elif cnt == max_value:
        result.append(i)

print(*result)