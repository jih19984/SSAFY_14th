# 문제
"""
상냥이는 스티커를 2N개 구매
스티커는 2행 n열로 배치되어 있다.

스티커 한 장을 떼면 변을 공유하는 스티커는 모두 찢어져 사용할 수 없게 된다.

따라서 상냥이는 각 스티커에 점수를 매기고 점수의 합이 최대가 되게 스티커를 떼어내려고 한다.
"""

# 풀이 방법
"""
1 <= n <= 100,000

n이 매우 크기 때문에 dfs로 불가능
dp를 생각해보자.
어떻게 스티커를 떼어내야 최대 점수가 나올까?

- 대각선으로 가는 경우 (지그재그)
- 하나의 열을 지나쳐 가는 경우 (왜 건너편의 다른 행에 있는 값이 매우 클 경우도 고려해야하기 때문)
input sample
7
10 30 10 50 100 20 40
20 40 30 50 60 20 80
n = 1 dp[0][0] = 20 dp[1][0] = 20
n = 2 dp[0][1] = dp[1][0] + arr[0][1]
...

n = k 
dp[0][k-1] = max(dp[1][k-2] + arr[0][k-1], dp[1][k-3] + arr[0][k-1])
dp[1][k-1] = max(dp[0][k-2] + arr[1][k-1], dp[0][k-3] + arr[1][k-1])
"""

import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())

    arrs = [list(map(int, input().split())) for _ in range(2)]
    dp = [[0] * (N) for _ in range(2)]
    if N >= 1:
        dp[0][0] = arrs[0][0]
        dp[1][0] = arrs[1][0]
    if N >= 2:
        dp[0][1] = arrs[0][1] + dp[1][0]
        dp[1][1] = arrs[1][1] + dp[0][0]

    for i in range(2, N):
        for j in range(2):
            if j == 0:
                dp[j][i] = max(dp[1][i-1] + arrs[0][i], dp[1][i-2] + arrs[0][i])
            else:
                dp[j][i] = max(dp[0][i-1] + arrs[1][i], dp[0][i-2] + arrs[1][i])

    print(max(dp[0][N-1], dp[1][N-1]))