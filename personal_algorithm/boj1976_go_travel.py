# 문제
"""
도시 N개 존재, 두 도시 사이에 길이 있을 수도 없을 수도 있음.
- 같은 도시를 여러 번 방문하기 가능

sample input
3 N: 도시의 수 <= 200
3 M: 여행 계획에 속한 도시의 수 <= 1000
0 1 0 NxN 배열
1 0 1
0 1 0
1 2 3 여행 계획

sample output
가능하면 YES, 불가능하면 NO 출력
"""

# 풀이 방법
"""
어떻게 풀 것인가?
dfs로 각 행 별 방문 여부를 저장후
다음 행으로 내려감.
이 때 방문하지 않은 경우에만 DFS로 다음 행으로 감을 주의
"""
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())   

# 인접 행렬 입력
graph = [list(map(int, input().split())) for _ in range(N)]

plan = list(map(int, input().split()))
plan = [p-1 for p in plan]  # 인덱스를 0부터 쓰기 위해 -1 처리
visited = [False] * N

def dfs(v):
    visited[v] = True
    for nxt in range(N):
        if graph[v][nxt] == 1 and not visited[nxt]:
            dfs(nxt)

# 여행 계획의 첫 번째 도시에서 DFS 시작
dfs(plan[0])

# 여행 계획에 포함된 도시들이 모두 방문됐는지 확인
possible = all(visited[city] for city in plan)

print("YES" if possible else "NO")