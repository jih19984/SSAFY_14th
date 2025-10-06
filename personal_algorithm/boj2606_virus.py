# 문제
"""
신종 바이러스는 네트워크를 통해 전파된다.

- 첫째 줄에 컴퓨터의 수가 주어진다
- 네트워크 상에 연결된 컴퓨터 쌍의 수가 주어진다.

1번 컴퓨터가 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하시오.

-> 문제의 조건을 항상 잘 읽자!!
--> pair = 0일때 고려 안해서 계속 틀림
"""

import sys
input = sys.stdin.readline

def dfs(st):
    for adj in graph[st]:
        if not visited[adj]:
            visited[adj] = 1
            dfs(adj)

    return None


N = int(input())
pair = int(input())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)
# 인덱스를 출발 지점으로 리스트에 저장

for _ in range(pair):
    st, en = map(int, input().split())
    graph[st].append(en)
    graph[en].append(st)

if pair == 0:
    print(0)
else:
    dfs(1)
    print(f"{visited.count(1) - 1}")

