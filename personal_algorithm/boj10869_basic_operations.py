# 문제
"""
두 자연수 A와 B가 주어진다. 이때, A+B, A-B, A*B, A/B(몫), A%B(나머지)를 출력하는 프로그램을 작성하시오. 
"""

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

print(f"{A+B}")
print(f"{A-B}")
print(f"{A*B}")
print(f"{A//B}")
print(f"{A%B}")
