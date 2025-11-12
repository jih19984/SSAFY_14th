# 문제
"""
start 11:53
end: 12:20
다리 놓기 
동쪽과 서쪽으로 나누는 큰 일직선 모양의 강이 흐르고 있음.

- 사이트: 강 주변에서 다리를 짓기에 적합한 곳
- 다리를 최대한 많이 짓는 것이 목표
- 다리는 서로 겹쳐질 수 없다!

다리를 지을 수 있는 경우의 수를 구해라!
"""

# 풀이 방법
"""
input
T
서쪽 N, 동쪽 M (0 <= N <= M <= 30)

for문을 돌려서
1. 첫번째 동쪽 사이트의 지점을 하나 선택 후
2. 나머지 사이트들 중에 연결될 수 있는 다리의 경우의 수 구하기!
-> 이때 경우의 수는 항상 앞에 수보다 뒤에 수가 커야함!
"""

import sys
input = sys.stdin.readline

# combinations용 변수
N = 3

def combinations(cnt, st, num):
    global total

    if cnt == N:
        total += 1
        return
    
    for idx in range(st, num):
        tmp.append(idx)
        combinations(cnt+1, idx+1, num)
        tmp.pop()

# combinations(0, 0, 6)
# print(result)

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    result = []
    tmp = []
    total = 0

    if N == M:
        total = 1
    else:
        combinations(0, 0, M)
    
    print(total)