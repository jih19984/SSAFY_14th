# 문제
"""
수열 A가 주어졌을 때 그 수열의 증가하는 부분 수열 중에서 합이 가장 큰 것을 구하는 프로그램을 작성하시오.
1, 100, 2, 50, 60, 3, 5, 6, 7, 8 인 경우에 합이 가장 큰 중가하하는 부분 수열은
1 2 50 60 -> 113이다.
"""

# 풀이 방법
"""
수열 A의 크기 (1 <= N <= 1,000)
수열 A를 이루고 있는 Ai가 주어진다. (1 <= Ai <= 1000)

핵심 개념
1. 각 dp배열에 초기값을 해당 위치의 수열값을 넣어줌.
2. i는 끝의 값, j는 i 이전의 값
"""
import sys

input = sys.stdin.readline

N = int(input())

sequence = list(map(int, input().split()))

dp = [0] * N

for i in range(N):
    dp[i] = sequence[i]

for i in range(1, N):
    for j in range(i):
        if sequence[j] < sequence[i]:  # 증가하는 경우
            dp[i] = max(dp[i], dp[j] + sequence[i])

print(max(dp))
