# 문제
"""
N개의 자연수와 자연수 M이 주어졌을 때 아래 조건을 만족하는 길이가 M인 수열을 모두 구하시오.

- N개의 자연수 중에서 M개를 고른 수열
- 중복되는 수열을 여러 번 출력하면 안됨
- 수열은 사전 순으로 증가
"""
import sys
input = sys.stdin.readline

def dfs(cnt):
    global M
    if cnt == M:
        print(*result)
        return
    
    for i in range(N):
        if not visited[i]:
            result.append(nums[i])
            visited[i] = 1
            dfs(cnt+1)
            result.pop()
            visited[i] = 0

N, M = map(int, input().split())

nums = list(map(int, input().split()))
nums.sort()

result = []
visited = [0] * N
dfs(0)