# 문제
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

- 1부터 N까지 자연수 중에서 M개를 고른 수열
- 같은 수를 여러번 골라도 okay
- 고른 수열은 비내림차순이어야 한다.
a1 <= a2 <= a3 <= a4 ...

수열의 다음 값은 항상 이전 값보다 크거나 같아야 하므로
dfs에서 다음 값의 시작구간을 인자로 받아 넘겨준다.
"""

import sys
input = sys.stdin.readline

def dfs(cnt, idx):
    global M
    if cnt == M:
        print(*result)
        return
    
    for i in range(idx, N+1):
        result.append(i)
        dfs(cnt+1, i)
        result.pop()



N, M = map(int, input().split())
result = []
dfs(0, 1)