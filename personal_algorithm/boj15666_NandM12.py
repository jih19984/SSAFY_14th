# 문제
"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이 M인 수열을 작성하시오.

- 중복되는 수열 출력 X
- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다.
- 비내림차순 순열
    a1 <= a2 <= a3 <= ... <= ak
"""

import sys
input = sys.stdin.readline

def dfs(cnt, idx):
    if cnt == M:
        res_tup = tuple(result)
        if res_tup not in total_result:
            total_result.add(res_tup)
        return    

    for i in range(idx, N+1):
        result.append(nums[i-1])
        dfs(cnt+1, i)
        result.pop()


N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []
total_result = set()

dfs(0, 1)

for res in sorted(total_result):
    print(*res)