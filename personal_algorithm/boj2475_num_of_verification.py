# 문제
"""
00000 ~ 99999 까지의 고유번호 뒤에 검증수가 들어간다.
검증수는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.

첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하니씩 주어질 때,
첫째 줄에 검증수를 출력해라.
"""

import sys
input = sys.stdin.readline

num_verify = list(map(int, input().split()))
result = 0 # 검증수 초기 할당

for i in range(len(num_verify)):
    result += num_verify[i]**2

final_result = result % 10

print(final_result)



