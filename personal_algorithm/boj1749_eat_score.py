# 문제
"""
N X M 행렬 존재
각 칸의 값은 -10,000 ~ 10,000

행렬의 부분행렬을 그려 그 안에 적힌 정수의 합을 구하시오.
-> 정수의 합은 최대!
"""

# 풀이 방법
"""
2    3  -21  -22  -23
5    6  -22  -23  -25
-22 -23  4    10   2
10   10  10   10   10
10   10  10   10   10

누적합을 이용해 dp배열 생성

문제!
사각형의 크기가 정해져 있지 않다

"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * (M+1) for _ in range(N+1)]

# 1단계: dp 배열 생성
for r in range(1, N+1):
    for c in range(1, M+1):
        dp[r][c] = dp[r-1][c] + dp[r][c-1] - dp[r-1][c-1] + arr[r-1][c-1]

# dp 배열 생성 체크
# for dps in dp:
#     print(*dps)


# 2단계 for문으로 dp배열 순회
# dp 배열의 인덱스를 숫자로 접근할 수 있게 변환해야한다!
# idx = N * M + M  r = 5 c = 5 인덱스가 20인 값의 행과 열은? 20/5 = 4 ... 0 -> 5행 1열
# N = 3 M = 5
# 2행 2열 -> 2*2 + 2 -> 6을 5로 나누면 몫 1 나머지 1 

# 여기서 r, c는 디피 배열에 1,1 기준 접근
# 전체 인덱스는 N * M + M
# best 값은 큰 값이 나오면 갱신

# 왜 16이 안나오지
# 무조건 터짐,,, 40000 * 40000 = 1,600,000,000

best = float('-inf')

for idx1 in range(1, N * M + 1):
    for idx2 in range(1+idx1, N * M + 1):
        r1 = (idx1-1) // M + 1
        c1 = (idx1-1) % M + 1
        r2 = (idx2-1) // M + 1
        c2 = (idx2-1) % M + 1

        if r1 >= r2 or c1 >= c2:
            continue

        total = dp[r2][c2] - dp[r1-1][c2] - dp[r2][c1-1] + dp[r1-1][c1-1]

        if total > best:
            best = total

print(best)



