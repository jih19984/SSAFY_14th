# 문제
"""
오늘은 민경이의 생일이다.
준협이는 생일을 맞아 민경이에게 요트를 선물로 줬다.
요트 선착장에는 G개의 번호가 있다.
선착장에는 P개의 요트가 순서대로 도착할 예정이며,
소여니는 i번째 요트를 1번부터 gi(1<= gi <= G)번째 게이트중 하나에 영구적으로 정박하려고 한다
요트가 어느 선착장에도 정박할 수 없다면 선착장은 폐쇄되고, 이후 어떤 요트도 도착할 수 없다.

소여니가 가장 많은 요트를 선착장에 정박시키면 현준이가 요트를 한 대 더 준다고 한다.
소여니는 요트를 최대 몇 개 정박시킬 수 있는가?

1 <= G <= 10^5
1 <= P <= 10^5
P개의 줄에 걸쳐 gi가 주어진다.
"""

# 풀이 방법
"""
문제를 먼저 이해해보자

3번째 줄부터 주어지는 값은 게이트 번호이다!

G = 4
P = 6

2 2 3 3 4 4

1~2 1~2 1~3 1~3 1~4 1~4

3번에서 끝남

G = 10
P = 8

1~4 1~6 1~4 1~5 1~7 1~8 1~2 1~9

1번째 요트를 4번
2번째 요트를 6번
3번째 요트를 3번
4번째 요트를 5번
5번째 요트를 7번
6번째 요트를 8번
7번째 요트를 2번
8번째 요트를 9번

가장 좋은 방법은 갈 수 있는 선착장의 번호 중 높은 것 먼저 리스트에 포함시킨다.
만약에 중복이 발생하면 그 때 카운트를 멈춘다.
"""

# 1번째 시도
"""
시간초과 발생
"""
# import sys
# input = sys.stdin.readline

# G = int(input())
# P = int(input())
# arr = set()
# cnt = 0

# P가 10만번인데 range로 만드는 과정이 10만번
# 따라서 10^10으로 시간초과
# for _ in range(P):
#     boat_num = int(input())
#     boat_range = set(range(1, boat_num+1))

#     if len(arr) == 0:
#         cnt += 1
#         arr.add(boat_num)
#     elif boat_range <= arr:
#         continue
#     else:
#         cnt += 1
#         arr.add(max(boat_range - arr))

# print(cnt)

# 2번째 시도
"""
유니온 파인드를 통해
선착장의 범위 값 중 가장 큰 값을 넣고
parent로 부모를 찾아가는 방식
"""

import sys
input = sys.stdin.readline

class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n
        
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    def union(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        
        # 대표자가 같다면 같은 집합
        if root_a == root_b:
            return
        
        # 대표자가 다르다면
        if self.rank[root_a] > self.rank[root_b]:
            self.parent[root_b] = root_a
            
        else:
            self.parent[root_a] = root_b
            if self.rank[root_a] == self.rank[root_b]:
                self.rank[root_a] += 1


G = int(input())
P = int(input())

uf = UnionFind(G+2)
cnt = 0

# 가장 큰 게이트의 번호를 먼저 받아오고
# 이후 1작은 값을 자식으로 갖는다.
"""
5 -> 2 -> 4

parent[5] = 5 -> union -> parent[5] = 4
parent[2] = 2 -> union -> parent[2] = 1
parent[2] = 1 -> union -> parent[2] = 0
parent[3] = 3 -> union -> parent[3] = 2
parent[3] = 2 -> parent[2] -> 0 따라서 break
"""
for _ in range(P):
    boat = int(input())

    gate_num = uf.find(boat)

    if gate_num == 0: # gate 번호 다 씀
        break

    uf.union(gate_num, gate_num-1)
    cnt += 1

print(cnt)
