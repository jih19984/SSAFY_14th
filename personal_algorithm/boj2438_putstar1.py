# 문제
"""
첫째 줄에 별 1개
둘째 줄에 별 2개
N번째 줄에 별 N개를 출력하시오.
"""

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, N+1):
    for _ in range(i):
        print('*', end='')
    print()