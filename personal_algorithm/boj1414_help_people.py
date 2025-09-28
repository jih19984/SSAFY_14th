# 문제
"""
N개의 방이 존재
각각의 방에는 모두 한 개의 컴퓨터가 있다.
이때 각 컴퓨터는 서로 연결되어 있어야 통신 가능

랜선의 길이
a ~ z : 1 ~ 26
A ~ Z : 27 ~ 52

N개의 컴퓨터가 연결되어 있는 랜선의 길이가 주어질 때
다솜이가 기부할 수 있는 랜선의 길이의 최댓값을 출력하시오.

"""
# 풀이 방법
"""
고속도로와 똑같은 kruskal을 이용해 푸는 MST 문제
서로 연결이라고해서 반드시 두 간선이 양방향이어야 하나? 문제의 의도가 아님
"""
import sys
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

def kruskal(edges, uf, n):
    edges.sort()
    added_cost = 0
    cnt = 0
    for cost, u, v in edges:
        if uf.union(u, v):
            added_cost += cost
            cnt += 1
            if cnt == n-1:  # MST 완성
                break
    return added_cost, cnt

def char_to_cost(ch):
    if ch.islower():
        return ord(ch) - 96
    elif ch.isupper():
        return ord(ch) - 38
    else:
        return 0

N = int(input().strip())
uf = UnionFind(N)
edges = []
all_len = 0

for i in range(N):
    row = input().strip()
    for j in range(N):
        cost = char_to_cost(row[j])
        all_len += cost
        if i != j and cost > 0:   # 자기 자신 제외, 간선만 추가
            edges.append((cost, i, j))

mst_cost, cnt = kruskal(edges, uf, N)

# 모든 컴퓨터 연결 실패
if cnt < N-1:
    print(-1)
else:
    print(all_len - mst_cost)