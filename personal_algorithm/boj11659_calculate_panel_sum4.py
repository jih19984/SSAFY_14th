# 문제
"""
수 N개가 주어졌을 때, i번째부터 j번째 수까지 합을 구하는
프로그램을 작성하시오.

N은 1 ~ 100,000
M은 1 ~ 100,000
"""

# 풀이 방법
"""
만약에 그냥 입력 받은 값을 sum으로 더하게 된다면
N과 M의 범위가 10만이하의 자연수이므로
10e6 * 10e6으로 무조건 시간 초과가 발생

누적합을 이용하자
각 인덱스에 1부터 해당 인덱스까지의 합을 저장
2:5 -> 1:5 - 1:2
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
lst = list(map(int, input().split()))
prefix = [0] * (N+1)

for i in range(1, N+1):
    prefix[i] = prefix[i-1] + lst[i-1]

for i in range(M):
    st, en = map(int, input().split())
    print(prefix[en] - prefix[st-1])