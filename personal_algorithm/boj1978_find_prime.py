# 문제
"""
주어진 N개의 수 중에서 소수가 몇 개인지 찾아 출력하시오.
N은 100이하
주어진 수의 범위는 1000이하
"""

import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int ,input().split()))
cnt = 0

for num in nums:
    if num == 1:
        continue
    elif num == 2 or num == 3:
        cnt += 1
    # 110의 제곱근은 대략 10.xxx
    # 그렇다면 110을 두 수의 곱으로 나타내면 하나는 반드시 10.xx보다 작거나 같음.
    # 따라서 2부터 10까지 모두 나누어 떨어지는 수가 있는지 확인
    check_num = int(num ** 0.5)
    for i in range(2, check_num+1):
        if num % i == 0:
            break
        if i == check_num:
            cnt += 1

print(cnt)

