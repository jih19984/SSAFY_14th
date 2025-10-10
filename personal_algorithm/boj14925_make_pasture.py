# 문제
"""
2차원 배열이 주어질 때,
가장 큰 정사각형의 한 변의 길이를 구하시오.
"""

# 풀이 방법
"""
all로 하면 무조건 터짐 10 ^ 4

정사각형 -> 이 문제에서는 정사각형의 넓이를 dp로 어떻게 구할 것인지 핵심
현재 좌표 기준 북서 대각선, 상, 좌의 dp배열(우하단기준) 중 최소값에 + 1(기존 사각형 길이) 더하면 길이를 구할 수 있다.
"""
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(N)]

dp = [[0] * M for _ in range(N)]
result = 0

# 사각형의 우하단 기준 dp 배열 생성
for i in range(N):
    for j in range(M):
        if grid[i][j] == 0:
            # 초기 dp 설정
            if i == 0 or j == 0:
                dp[i][j] = 1
            # dp배열 중 모두가 1이상이어야 1이나오고 2이상일 때 2가 나와야한다.
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
            result = max(result, dp[i][j])

print(result)