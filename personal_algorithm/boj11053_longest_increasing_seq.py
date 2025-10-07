# 문제
"""
수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하는 프로그램을 작성하시오.
ex)
A = 10 20 10 30 20 50
10 20 30 50이 가장 긴 부분수열이고 길이는 4이다.

1 <= N <= 1,000
1 <= an <= 1,000
"""

# 풀이 방법
"""
모든 부분집합을 구할까?
-> 2^1000으로 절대 안돼. 비트마스크 X

코드 작성하다보니 생각이 너무 엉킴...
다시 정리해보면
1. 각 dp의 인덱스에 수열의 길이를 저장(작은 수를 만나면 1부터 다시 시작)
2. 이 때 dp[j]+1의 값이 이전 최대값인 dp[i]보다 크다면 갱신
3. 전체 dp에서 가장 큰 값을 출력
"""
import sys
input = sys.stdin.readline

N = int(input())

seq = list(map(int, input().split()))

dp = [1] * (N)

for i in range(N):
    for j in range(i):
        if seq[j] < seq[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))