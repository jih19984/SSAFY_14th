# 문제
"""
비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.
add: S에 x를 추가
remove: S에서 x를 제거
check x: S에 x가 있으면 1 없으면 0 출력
toggle x: S에 x가 있으면 x를 제거하고, 없으면 x를 추가
all: S를 {1, 2, ... 20}으로 바꾼다
empty: S를 공집합으로 바꾼다

M은 3,000,000이하의 자연수

remove는 집합에 존재하는 원소를 지우는 동작에 사용
discard는 집합에 존재하지 않음을 보장하려고 할 때 사용
"""

import sys
input = sys.stdin.readline

M = int(input())
result = set()
for _ in range(M):
    op = input().strip()
    if op == 'all':
        result = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20}
        continue

    if op == 'empty':
        result = set()
        continue
    
    else:
        op, num = op.split()
        num = int(num)
        if op == 'add':
            result.add(num)
        elif op == 'check':
            if num in result:
                print(1)
            else:
                print(0)
        elif op == 'toggle':
            if num in result:
                result.remove(num)
            else:
                result.add(num)
        else:
            result.discard(num)
    



