# 문제
"""
N을 입력받은 뒤, 구구단 N단을 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')