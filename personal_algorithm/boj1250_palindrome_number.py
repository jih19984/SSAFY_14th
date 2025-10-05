# 문제
"""
어떤 수를 앞에서 또는 뒤에서 읽어도 똑같다면, 그 단어를 펠린드롬이라고 한다.

각 줄 마다 주어진 수가 펠린드롬수이면 'yes, 아니면 'no'를 출력하시오.
"""

import sys
input = sys.stdin.readline

while True:
    strs = str(input().strip())
    strs_len = len(strs)
    check = True

    if strs == '0':
        break

    for i in range(strs_len//2):
        if strs[i] == strs[strs_len-1-i]:
            continue
        else:
            check = False
            break

    if check == True:
        print('yes')
    else:
        print('no')