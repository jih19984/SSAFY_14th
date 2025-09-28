# 문제
"""
도시 철도가 이미 설치되어 있는데
추가로 도시 철도를 설치하되 총 비용을 최소화해라

- 비용이 음수인 경우: 이미 설치된 도로
- 비용이 1000인 경우: 가중치가 제일 높으므로 최대한 고려하지 않아야 함.

sample input
5
   0  -10 1000  -20 1000
 -10    0   10  -30 1000
1000   10    0   30   10
 -20  -30   30    0   20
1000 1000   10   20    0

sample output
80 2 고속도로 철치 총 비용, 새로이 설치한 철도 개수
2 3 고속도로가 설치된 두 도시 번호
3 5 ''
"""

# 풀이 방법
"""
총 비용을 최소화하여 최소 신장 트리를 만드는 것이 목표
기존에 연결된 간선들의 집합이 있다는 것을 고려!
kruskal 쓰면 바로 풀릴듯?
"""
# Kruskal
"""
1. 간선들을 가중치 기준으로 오름차순 정렬
2. 가장 작은 가중치 간선부터 하나씩 꺼내면서
    두 정점이 같은 집합에 속하지 않으면 그 간선을 MST에 포함
    이미 같은 집합이라면 (사이클이 생긴다면) 무시
3. 모든 정점을 연결할 때까지 반복
"""

import sys
input = sys.stdin.readline

class UnionFind:
    # 생성자 메서드. 클래스가 인스턴스화 될 때 한 번 시행
    def __init__(self, size):
        self.root = [i for i in range(size)]
        self.rank = [1] * size
    
    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx == ry:
            return False
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return True

def kruskal_with_existing(n, edges, uf, base_cost):
    edges.sort()
    new_edges = []
    added_cost = 0

    for cost, u, v in edges:
        if uf.union(u, v):
            added_cost += cost
            new_edges.append((u, v))
    total_cost = base_cost + added_cost
    return total_cost, new_edges

N = int(input().strip())
uf = UnionFind(N)
edges = []
base_cost = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(i+1, N):
        cost = row[j]
        if cost < 0:
            # 이미 설치된 도로 비용은 총비용에 포함
            base_cost += abs(cost)
            uf.union(i, j)
        elif cost > 0:
            edges.append((cost, i, j))

total_cost, new_edges = kruskal_with_existing(N, edges, uf, base_cost)

# 출력
print(total_cost, len(new_edges))

for u, v in new_edges:
    print(u+1, v+1) 