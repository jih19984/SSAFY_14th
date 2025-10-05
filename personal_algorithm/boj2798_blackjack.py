# 문제
"""
새로운 블랙잭 규칙
- 각 카드에는 양의 정수가 쓰여 있음
- 딜러는 N장의 카드를 모두 숫자가 보이도록 바닥에 놓음
- 그 후 딜러는 숫자 M을 외침
- 이 후 플레이어는 N장의 카드 중 3장의 카드를 골라야 한다!
- 이 때 3장의 카드 합은 M을 넘지 않으면서 M가 최대한 가깝게 만들어야 한다.

-> M가 가장 가까운 세 장의 카드 최대 합을 구하시오.
"""

import sys
input = sys.stdin.readline

def dfs(cnt, result):
    global M, best
    if cnt == 3:
        if result <= M:
            best = max(best, result)
        return
    
    if result > M:
        return
    
    for i in range(len(cards)):
        if not visited[i]:
            visited[i] = 1
            dfs(cnt+1, result + cards[i])
            visited[i] = 0

N, M = map(int, input().split())
cards = list(map(int, input().split()))
visited = [0] * (N+1)
best = float('-inf')
dfs(0,0)
print(best)