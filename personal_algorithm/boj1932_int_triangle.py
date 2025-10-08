# 문제
"""
합이 최대가 되는 경로에 있는 수의 합을 구하라
1 <= N <= 500
"""

# 풀이 방법
"""
sample을 보자
N = 5
7       dp[1] : 7 
3 8     dp[2] = dp[1] + arr[1][0], dp[3] = dp[1] + arr[1][1]
8 1 0   
dp[4] = dp[2] + arr[2][0] 
dp[5]= max(dp[2] + arr[2][1], dp[3] + arr[2][1]), 
dp[6] = dp[3] + arr[2][2] 
2 7 4 4 
4 5 2 6 5   

"""

import sys
input = sys.stdin.readline

N = int(input())
tris = [list(map(int, input().split())) for _ in range(N)]

# 1차원 dp는 할 게 못된다...
"""
2차원 dp로 전환
"""
dp = [[0] * len(tris[i]) for i in range(N)]
dp[0][0] = tris[0][0]

for i in range(1, N):
    for j in range(len(tris[i])):
        if j == 0:
            dp[i][j] = dp[i-1][0] + tris[i][j]
        elif j == len(tris[i]) - 1:
            dp[i][j] = dp[i-1][j-1] + tris[i][j]
        else:
            dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + tris[i][j]

print(max(dp[-1]))



