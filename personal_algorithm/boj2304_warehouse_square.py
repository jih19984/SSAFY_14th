# 문제
"""
창고 다각형
start 11:44
end 12:26

직사각형들의 위치와 높이가 주어질 때
창고 다각형의 최소 면적을 구해라!
"""

import sys
from collections import deque

""" 1. 입력 """
input = sys.stdin.readline
N = int(input())
squares = []

for _ in range(N):
    x, h = map(int, input().split())
    squares.append((x, h))

""" 2. 높이 기준 정렬 """
squares.sort(key=lambda x: x[1])

""" 3. 높은 높이 먼저 pop해서 창고 다각형 면적 구하기 """
highest_x, highest_h = squares.pop()
left_x = highest_x
right_x = highest_x
area = highest_h

# pop한 높이와 가장 높은 높이 사이에 있는 모든 사각형을 보지 않는다.
while squares:
    cal_x, cal_h = squares.pop()

    if cal_x < left_x:
        area += (left_x-cal_x) * cal_h
        left_x = cal_x
    elif cal_x > right_x:
        area += (cal_x - right_x) * cal_h
        right_x = cal_x

print(area)

