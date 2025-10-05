# 문제
"""
온라인 저지에 가입한 사람들의 나이와 이름이 가입한 순서대로 주어진다.
이때, 회원들을 나이가 증가하는 순으로
나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하시오.

python은 튜플의 2개의 인자 중 첫번째 같으면 sort시 자동으로 두 번째 인자의 알파벳 순으로 나열.
"""

import sys
input = sys.stdin.readline

N = int(input())

member_lst = [list(map(str, input().strip().split())) for _ in range(N)]

member_lst.sort(key=lambda x:int(x[0]))

for i in range(N):
    print(f"{member_lst[i][0]} {member_lst[i][1]}")

