# 문제
"""
두 개의 자연수를 입력받아, 최대 공약수와 최소 공배수를 출력하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

# 최대 공약수
# 각 수의 제곱근을 구한 후
# 제곱근보다 작은 정수로 하나씩 나눠가며 나눠지는 수를 찾는다.

divisor_a = A
divisor_a_set = set()
for i in range(2, divisor_a + 1):
    if A % i == 0:
        divisor_a_set.add(i)

divisor_b = B
divisor_b_set = set()
for j in range(2, divisor_b + 1):
    if B % j == 0:
        divisor_b_set.add(j)

common_divisor = divisor_a_set & divisor_b_set
if not common_divisor:
    common_max_divisor = 1
else: 
    common_max_divisor = max(common_divisor)

# 최소 공배수
# A와 B의 배수 중 공통된 배수를 찾는 것
# A * B가 최대 공배수이다.

multiple_a = set([A * i for i in range(1, B+1)])
multiple_b = set([B * i for i in range(1, A+1)])

common_min_multiple = min(multiple_a & multiple_b)

print(common_max_divisor)
print(common_min_multiple)
