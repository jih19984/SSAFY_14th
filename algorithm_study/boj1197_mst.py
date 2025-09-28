# 문제
"""
최소 스패닝 트리
그래프가 주어졌을 때, 최소 스패닝 트리를 구하는 프로그램을 작성하시오.

V: 1 ~ 10,000
E: 1 ~ 100,000

sample input
3 3 V E
1 2 1 u, v, w
2 3 2
1 3 3

sample output: 최소 스패닝 트리 가중치
3
"""

# 풀이 방법
"""
Kruskal algorithm
가중치를 간선에 할당한 그래프의 모든 정점을 최소 비용으로 연결하여,
최적의 해답을 구하자

1. 그래프의 모든 간선들을 가중치의 오름차순으로 정렬
2. 정렬된 간선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
    a. 가장 낮은 가중치를 먼저 선택
    b. cycle을 형성하는 간선을 제외
3. 해당 간선을 현재의 MST 집합에 추가

다음 간선을 추가할 때 사이클을 생성하는 지 체크 -> union-find 알고리즘으로 구현
"""
import sys

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
            return True # 합쳐졌다면 True
        
        return False # 이미 같은 집합
    
def kruskal(n, edges):
    """
    n: 정점의 개수
    edges: (가중치, u, v) tuple 리스트
    """
    uf = UnionFind(n+1)
    mst_weight = 0
    mst_edges = []

    # 1. 간선들의 가중치 기준 정렬
    edges.sort()

    # 2. 간선 하나씩 확인
    for w, u, v in edges:
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight

V, E = map(int, input().split())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

print(kruskal(V, edges))