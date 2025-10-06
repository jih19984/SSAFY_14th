# 문제
"""
계단에는 일정한 점수가 쓰여있다.

계단을 오르는 규칙
- 계단은 한계단 또는 두계단을 오를 수 있다.
- 연속된 세 개의 계단을 모두 밟아서는 안된다. (한계단을 연속으로 오르기 불가, 연속으로 두계단은 가능)
- 마지막 도착 계단은 반드시 밟아야 한다.

계단을 오를 때 얻을 수 있는 총 점수의 최댓값을 구하시오.

계단의 개수: 300이하 자연수
점수: 10,000 이하의 자연수
"""

# 풀이 방법
"""
10 20 15 25 10 20 30 40 50 60 ...

7번째 인덱스까지가는 최댓값
dp[3] : 10 -> 20 -> 15
dp[4] : 10 -> 15 -> 25 or 10 -> 20 -> 25 : 55
dp[5] : dp[3] + 10 or dp[2] +25 + 10
dp[6] : dp[4] + 20 or dp[3] + 10 + 20


결국 이 문제의 핵심은
1칸은 연속으로 움직이지 못하기 때문에
끝점을 기준으로 3칸 전 위치에서 2칸 이동 후 1칸 이동하여 도착하거나
또는 2칸 전 위치에서 2칸 이동하여 도착하는 경우로 나뉠 수 있다.
"""

import sys
input = sys.stdin.readline

N = int(input())

stairs_scores = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = stairs_scores[0]
if N >= 2:
    dp[1] = dp[0] + stairs_scores[1]
if N >= 3:
    dp[2] = max(stairs_scores[0] + stairs_scores[2], stairs_scores[1] + stairs_scores[2])

for i in range(3, N):
    dp[i] = max(dp[i-2]+stairs_scores[i], dp[i-3]+stairs_scores[i-1]+stairs_scores[i])

print(dp[N-1])