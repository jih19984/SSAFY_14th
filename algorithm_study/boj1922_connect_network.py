# 문제
"""
네트워크 연결
- 모든 컴퓨터가 연결되어 있어야 한다
- 이 컴퓨터들을 연결하는 비용들이 주어졌을 때, 모든 컴퓨터를 연결하는데 필요한 최소비용을 출력해라
- 모든 컴퓨터를 연결할 수 없는 경우는 없다.

sample input
- 컴퓨터의 수 N 1 ~ 1000
- 선의 수 M 1 ~ 100000
- M개의 줄에 걸쳐 컴퓨터를 연결하는 데 드는 비용 (u, v, w)
6
9
1 2 5
1 3 4
2 3 2
"""

# 풀이 방법
"""
krusukal 쓰자
가중치를 간선에 할당한 그래프의 모든 정점을 최소 비용으로 연결하여
최적의 해답을 구하자

1. 그래프의 모든 간선들을 가중치의 오름차순으로 정렬
2. 정렬된 가선 리스트에서 순서대로 사이클을 형성하지 않는 간선을 선택
    - 가장 낮은 가중치를 먼저 선택
    - cycle을 형성하는 간선 제외
3. 해당 간선을 현재의 MST에 추가

다음 간선을 추가할 때마다 사이클 생성하는지 유니온 파인드를 통해 체크
"""

import sys

class UnionFind:
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size

    def find(self, x):
        # node x의 부모가 x가 아니라면
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
    '''
    n: 정점의 개수
    edges: (u, v, w)
    '''
    uf = UnionFind(n+1)
    mst_weight = 0

    # 1. 간선들의 가중치 기준 정렬
    edges.sort()

    # 2. 간선 하나씩 확인
    for w, u, v in edges:
        if uf.union(u, v):
            mst_weight += w
    
    return mst_weight

V = int(input())
E = int(input())
edges = []

for _ in range(E):
    u, v, w = map(int, input().split())
    edges.append((w, u, v))

print(kruskal(V, edges))