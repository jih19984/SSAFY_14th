# 문제
"""
1x2, 2x1 타일로 2xn 크기의 직사각형을 채우는 방법의 수를 구하시오.
"""

# 풀이
"""
n = 1 -> 1
n = 2 -> 2
n = 3 -> 2x1 3개, 2x1 1개, 1x2 2개: 2가지 -> 3가지
n = 4 -> dp[n] = dp[n-1] + dp[n-2]

그림을 그려보면서 규칙을 찾는 것이 가장 직관적

문제좀 읽자... 10,007로 안나누다니...
"""

import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 1001
dp[1] = 1
dp[2] = 2
for i in range(3, N+1):
    dp[i] = dp[i-1] + dp[i-2]

print(dp[N]% 10007)