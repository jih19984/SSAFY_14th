import heapq

def prim(n, graph):
    """
    n: 정점 개수
    graph: 인접 리스트 (u -> [비용, v],,,)
    """
    visited = [False] * n # 방문 여부
    mst_cost = 0 # MST 총 비용
    mst_edges = [] # MST 간선 기록

    # 최소 힙(비용, 현재 정점, 다음 정점)
    # 시작은 정점 0에서 출발

    heap = [(0, -1, 0)] # 간선 비용, 시작 노드, 도착 노드

    while heap:
        cost, u, v = heapq.heappop(heap)

        if visited[v]:
            continue
        visited[v] = True

        mst_cost += cost
        if u != -1: # 시작점 제외
            mst_edges.append((u, v, cost))
        
        # v에서 갈 수 있는 간선들 추가
        for next_cost, nxt in graph[v]:
            if not visited[nxt]:
                heapq.heappush(heap, (next_cost, v, nxt))
    
    # 모든 정점을 방문하지 못했다면 MST 불가능
    if not all(visited):
        return -1, []
    
    return mst_cost, mst_edges

n = 5
graph = [[] for _ in range(n)]
edges = [
    (0, 1, 2),
    (0, 3, 6),
    (1, 2, 3),
    (1, 3, 8),
    (1, 4, 5),
    (2, 4, 7),
    (3, 4, 9),
]

# 무방향 그래프이므로 양쪽에 다 추가
for u, v, w in edges:
    graph[u].append((w, v))
    graph[v].append((w, u))

mst_cost, mst_edges = prim(n, graph)

print("MST 총 비용:", mst_cost)
print("MST 간선들:", mst_edges)
