# 문제
"""
크기 N x N인 도시가 존재
도시는 1 x 1 크기의 칸으로 나누어져 있다.

빈칸: 0, 집: 1, 치킨: 2
치킨거리는 집과 가장 가까운 치킨집 사이의 거리
치킨거리: 집을 기준으로 정해짐 -> abs(r1-r2) + abs(c1-c2)

도시의 치킨 거리 = 모든 집의 치킨 거리의 합

일부 치킨 집을 폐업시키려고 한다.
도시에 있는 치킨 집 중 M개를 고르고 나머지는 모두 폐업 시킬 때
어떻게 고르면 도시의 치킨 거리가 가장 작을 것인가?

도시의 치킨 거리의 최솟값을 출력하시오.
"""

# 풀이 방법
"""
M개의 치킨 집을 조합으로 선택한 후
집에서 해당 치킨 집까지 가는 치킨 거리를 다 더한다.

그리고 이 조합 중 가장 최소 도시 치킨 거리를 구한다.

combination 함수 만들 때
visited 안써도 되는 것과 idx가 아닌 i를 인자로 받는 것에 유의
애초에 인덱스를 뒤로 한 칸 밀어서 하기 때문에 visited 불필요!
"""

import sys
from collections import deque
input = sys.stdin.readline

def comb(cnt, idx):
    global total_chicken

    if cnt == M:
        total_result.append(result[:])
        return
    
    for i in range(idx, len(en_idx)):
        result.append(en_idx[i])
        comb(cnt+1, i+1)
        result.pop()

# 치킨 거리 계산
def calculate(r1, c1, r2, c2):
    dist = abs(r1-r2) + abs(c1-c2)
    return dist

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
st_idx = [] # 집
en_idx = [] # 치킨
result = [] # comb 구하기 위한 임시 리스트
total_result = [] # 조합을 담은 리스트
best = 1000000
tmp = 0
ans = 0

# 집의 위치 찾기
for r in range(N):
    for c in range(N):
        if arr[r][c] == 1:
            st_idx.append((r,c))
        if arr[r][c] == 2:
            en_idx.append((r,c))

total_chicken = len(en_idx) - M
comb(0, 0)

# total_result 순회하며 가장 최소 치킨 도시 거리 찾기
for com in total_result:
    tmp = 0
    for st in st_idx:
        dist = 1000000
        for en in com:
            dist = min(dist, calculate(st[0],st[1],en[0],en[1]))
        tmp += dist
    best = min(best, tmp)

print(best)
