# 문제
"""
종이의 가로 길이, 세로 길이를 입력받는다.
잘라야 할 점선들이 주어질 때, 가장 큰 종이 조각의 넓이는 몇인가?

가로: 0
세로: 1

sample input
10 8 (가로, 세로)
3   (자르는 선의 개수)
0 3
1 4
0 2

sample output
30
"""

# 풀이 방법
"""
1. 가로와 세로를 나눠서 리스트에 담는다.
2. 각 가로 리스트와 세로 리스트에 0과 각 가로 or 세로의 최대 크기를 넣어준다.
3. 각 리스트를 정렬 
4. 가로 리스트 내의 요소들끼리 차이 중 가장 큰 값 * 세로 리스트 내 요소들끼리 차이 중 가장 큰 값 곱해 최대 넓이를 구한다.
"""

import sys
from collections import deque
input = sys.stdin.readline

C, R = map(int, input().split())

num = int(input())
cut_lst = [list(map(int, input().split())) for _ in range(num)]
r_lst = deque([0])
c_lst = deque([0])
r_diff = deque([])
c_diff = deque([])

for dir, loc in cut_lst:
    if dir == 0:
        r_lst.append(loc)
    else:
        c_lst.append(loc)

r_lst.append(R)
c_lst.append(C)
r_lst = sorted(r_lst)
c_lst = sorted(c_lst)

for i in range(1, len(r_lst)):
    r_diff.append(r_lst[i] - r_lst[i-1])

for j in range(1, len(c_lst)):
    c_diff.append(c_lst[j] - c_lst[j-1])

print(max(r_diff) * max(c_diff))
