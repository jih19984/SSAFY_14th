# 문제
"""
주어진 세 변의 길이로 삼각형이 직각인지 아닌지 구분하시오.
맞다면 right을 아니라면 wrong을 출력하시오.
"""

import sys
input = sys.stdin.readline

while True:
    len_set = {0, 1, 2}
    tri = list(map(int, input().split()))
    if tri[0] == 0 and tri[1] == 0 and tri[2] == 0:
        break
    tri.sort()
    if tri[0] ** 2 + tri[1] ** 2 == tri[2] ** 2:
        print('right')
    else:
        print('wrong')

