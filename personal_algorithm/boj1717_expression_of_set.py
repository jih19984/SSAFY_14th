# 문제
"""
초기에 n+1개의 집합 {0}, {1}, {2}, ... {n}이 존재
두 원소가 같은 집합에 포함되어 있는지를 확인하는 연산을 수행하려고 한다.
집합을 표현하는 프로그램을 작성하시오.

"""

# 풀이 방법
"""
집합의 연산 속도를 빠르게 수행하기 위한 알고리즘?
바로 유니온 파인드!

sample input
n, m n: 초기 집합의 개수로 쓰기 위한 수 m: 입력으로 주어지는 연산의 개수
7 8
0은 두 원소의 합집합
1은 두 원소가 같은 집합인지 확인
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

sample output
NO
NO
YES
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
            return True
        if self.rank[rx] > self.rank[ry]:
            self.root[ry] = rx
        elif self.rank[rx] < self.rank[ry]:
            self.root[rx] = ry
        else:
            self.root[ry] = rx
            self.rank[rx] += 1
        return False
    
n, m = map(int, input().split())
num_lst = [list(map(int, input().split())) for _ in range(m)]
uf = UnionFind(n+1)

for check, a , b in num_lst:
    if check == 0:
        uf.union(a, b)
    else:
        if uf.find(a) == uf.find(b):
            print("YES")
        else:
            print("NO")