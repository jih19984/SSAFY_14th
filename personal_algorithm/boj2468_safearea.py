# 문제
"""
물에 잠기지 않는 최대 안전 영역의 개수를 구하시오.
"""

# 풀이
"""
BFS를 돌리자!
최대 안전 영역의 개수를 구하는 것이므로,
강수량을 계속 증가시키면서 최대값 갱신
"""

import sys
input = sys.stdin.readline

N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]

