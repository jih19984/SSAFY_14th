# 문제
"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이 M인 수열을 작성하시오.
- N개의 자연수 중에서 M개를 고른 수열
- N개의 자연수에서 중복된 수가 있을 수 있음
- 중복되는 수열을 출력하면 안됨
"""

import sys
input = sys.stdin.readline

def dfs(cnt):

    if cnt == M:
        res_tup = tuple(result)
        if res_tup not in total_result:
            total_result.add(res_tup)  
        return
    
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = 1
            result.append(nums[i-1])
            dfs(cnt+1)
            visited[i] = 0
            result.pop()

N, M = map(int, input().split())
visited = [0] * (N+1)
nums = list(map(int, input().split()))

nums.sort()

total_result = set()
result = []

dfs(0)
# 파이썬은 sorted함수를 이용해 set을 정렬 가능
# set은 튜플과 같은 불변 객체를 요소로 가질 수 있다.
for res in sorted(total_result):
    print(*res)