# 문제
"""
2차원 배열이 주어졌을 때
(i, j)부터 (x, y)까지의 배열에 저장되어 있는 수들의 합을 구하시오

sample input
2 3 배열의 크기
1 2 4 배열
8 16 32
3 합의 구간
1 1 2 3
1 2 1 2
1 3 2 3

sample output
63
2
36
"""

# 풀이 방법
"""
좌표가 2개 들어왔을 때 범위 합 구하는 함수
array에 들어온 값은 R가 C가 반대임을 명심
300 * 300 * 10000 = 9 * 10^8 초 -> 9억
pypy는 보통 파이썬보다 루프 속도가 5~10배 빠름.
단순 구현은 시간 초과가 나므로 반드시 누적합을 이용해야함

누적합을 할 때 prefix 배열 헷갈리지 않게 주의!!
기존 배열보다 가로 세로의 크기를 +1해서 하기 때문에, 누적합 배열을 만들 때
prefix[i][j]에 array[i-1][j-1]을 더함!!
"""

import sys

input = sys.stdin.readline

R, C = map(int, input().split())

array = [list(map(int, input().split())) for _ in range(R)]
num_sum = int(input())

prefix = [[0]*(C+1) for _ in range(R+1)]

for i in range(1, R+1):
    for j in range(1, C+1):
        prefix[i][j] = (array[i-1][j-1] 
                        + prefix[i-1][j]  
                        + prefix[i][j-1] 
                        - prefix[i-1][j-1])

for _ in range(num_sum):
    x1, y1, x2, y2 = map(int, input().split())
    result = (prefix[x2][y2] 
              - prefix[x1-1][y2] 
              - prefix[x2][y1-1] 
              + prefix[x1-1][y1-1])
    print(result)
