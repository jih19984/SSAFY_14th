# 문제
"""
N x N 크기의 표에 수가 채워져있다.
(x1, y1), (x2, y2)까지 합을 구하는 프로그램을 작성하시오.

1 <= N <= 1024, 1 <= M <= 100,000
"""

# 풀이방법
"""
누적합을 dp 배열에 저장해야된다는 감이 온다
어떻게 누적합을 구할 것인가?
1 1 1 1
1 1 1 1
1 1 1 1
1 1 1 1
이 있을 때

좌측하단의 2x2크기의 사각형과 우상단의 2x2크기의 사각형을 더한 후 가운데 겹치는 부분을 뺀다.
마지막으로 좌상단에 채워진 값과 우하단에 채워진 값을 더하면 누적합이 나온다.

r1, c1, r2, c2 넓이를 어떻게 구할 것인가?
psum[r2][c2] - psum[r1-1][c2]-psum[r2][c1-1] +psum[r1-1][c1-1]

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
locs = [list(map(int, input().split())) for _ in range(M)]
dp = [[0] * (N+1) for _ in range(N+1)]

# r, c 까지의 합 구하기
for r in range(1, N+1):
    for c in range(1, N+1):
        dp[r][c] = arr[r-1][c-1] +dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1]

# r1,c1 부터 r2,c2 구하기
# 좌표가 x, y로 적혀있으나 문제를 잘 읽어보면 r, c와 동일
for r1, c1, r2, c2 in locs:
    result = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]
    print(result)