# 문제
"""
이항계수란?
이항식에서 이항 정리로 전개했을 때 각 항의 계수이며 주어진 크기의 순서가 없는 조합의 가짓수 
nCk = n!/((n-k)!k!)
0! = 1

자연수 N과 자연수 K가 주어졌을 때, 이항계수 (N K)를 구하시오.
"""

def factorial(n):
    if n == 1 or n == 0:
        return 1
    return n * factorial(n-1)

import sys
input = sys.stdin.readline

N, K = map(int, input().split())

print(int(factorial(N) / (factorial(N-K) * factorial(K))))

