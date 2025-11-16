# 문제
"""
start: 19:17
end: 20:51

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구해라.

예시)
A = {10, 20, 10, 30, 20, 50}
10, 20, 30, 50 -> 길이 4

수열 A의 길이: 1000
수열의 원소 크기 1이상 1000이하
"""

# 풀이 방법
"""
10, 20, 10, 30, 20, 50이 있으면,
dp[0] = 10
dp[1] = 10, 20
dp[2] = 10
dp[3] = 10, 20, 30
dp[4] = 10, 20
dp[5] = 10, 20, 30, 50

dp 배열에 개수를 우리가 구하고자하는 수열의 길이를 저장하고,
prev_dp 배열을 만들어서 가장 큰 길이의 수열의 이전 원소를 저장한다.
이후, prev_dp의 인덱스들을 연결하여 전체 수열을 구한다.
"""

import sys
input = sys.stdin.readline

N = int(input())
seq = list(map(int, input().split()))

dp = [1] * N
prev_dp = [-1] * N

# i는 마지막 값, j는 i 이전의 값
for i in range(1, N):
    for j in range(i):
        if seq[j] < seq[i]:
            # dp[j]의 값에 1더한 게 크다면 dp[i] 갱신
            if dp[j] + 1 > dp[i]:
                dp[i] = dp[j] + 1
                # i번째 원소 이전에 어떤 원소(j)를 선택했는지 저장
                prev_dp[i] = j

# 최장 길이와 마지막 인덱스 찾기
max_len = max(dp)
max_idx = dp.index(max_len)

result = []
idx = max_idx

# prev_dp의 인덱스들을 모두 연결하여 result 만들기
while idx != -1:
    result.append(seq[idx])
    idx = prev_dp[idx]

result.reverse()

print(max_len)
print(*result)






