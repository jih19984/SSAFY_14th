# 문제
"""
마을을 N개의 집과 M개의 길로 구성
- 길을 어느 방향으로든 다닐 수 있음
- 길 사이에는 유지비가 존재

마을의 이장은 마을을 두 개의 분리된 마을로 분할할 계획을 가지고 있음.
- 마을을 분할할 때는 각 분리된 마을 안에 집들이 서로 연결되도록 분할해야 한다.
- 각 분리된 마을 안에 임의의 두집 사이에 경로가 항상 존재해야 한다.

-> 마을의 이장은 임의의 두 집 사이에 경로가 존재하게 하되 길의 유지비의 합을 최소로 만들고자 한다.
sample input
7 12 N M
1 2 3   M개의 줄에 걸쳐 (u, v, w)
1 3 2
3 2 1
2 5 2
...
"""

# 풀이 방법
"""
MST 유형은 맞는데... 마을을 2개로 분할해야 하네?
kruskal 쓰면 된다!
문제에서 요구하는 건 없애고 남은 길 유지비의 최솟값!
즉, mst의 최소 가중치 합을 구한 뒤 가장 가중치가 큰 간선을 빼주면 끝
"""

import sys
# readline 안쓰면 시간초과 남
input = sys.stdin.readline

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)

        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.root[root_y] = root_x
        
            elif self.rank[root_x] < self.rank[root_y]:
                self.root[root_x] = root_y

            else:
                self.root[root_y] = root_x
                self.rank[root_x] += 1

            return True
        return False
    
def kruskal(n, edges):
    """
    정점의 개수: n
    간선들의 집합: edges = (w, u, v)
    """
    uf = UnionFind(n+1)
    edges.sort()
    mst_weight = 0
    max_edge = 0 # mst 안에서 가중치가 가장 큰 간선 기록

    for w, u, v in edges:
        if uf.union(u, v):
            mst_weight += w
            max_edge = max(max_edge, w)

    return mst_weight - max_edge

V, E = map(int, input().split())
edges = []
mst_weight_sum = 0

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))
    mst_weight_sum += w

print(kruskal(V, edges))
