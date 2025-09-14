# 문제
"""
루트없는 트리가 주어진다.
트리의 루트: 1
각 노드의 부모를 구하는 프로그램을 작성하시오.
(2번 노드부터 순서대로 출력)

<input>
- 노드의 개수: N
- N-1 줄에 걸쳐 트리 상에 연결된 두 정점의 개수
"""
from collections import deque
import sys

input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N+1)]

for _ in range(N-1):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)

# 부모 저장 리스트
parent = [0] * (N+1)

# BFS
st = 1
q = deque([st])

while q:
    nd = q.popleft()
    for nxt in graph[nd]:
        if not parent[nxt]:
            parent[nxt] = nd
            q.append(nxt)

for i in range(2, N+1): # N+1까지!!
    print(parent[i])
    