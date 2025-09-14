# 문제
"""
+, -, 괄호를 가지고 식을 만들었다.
그러나 괄호를 실수로 지워버림

괄호를 적절히 쳐서 이 식의 값을 최소로 만드시오.

조건
- 5자리보다 많이 연속되는 숫자 없음

-> 덧셈 먼저 다하기
-> eval 00009를 처리 못함
"""

import sys

input = sys.stdin.readline

exp = input().split('-')

result = sum(map(int, exp[0].split('+')))

for ele in exp[1:]:
    result -= sum(map(int, ele.split('+')))

print(result)

