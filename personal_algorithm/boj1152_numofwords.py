# 문제
"""
영어 대소문자와 공백으로 이루어진 문자열이 존재. 이 문자열에는 몇 개의 단어가 있을까?
- 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.
"""

import sys

input = sys.stdin.readline

strs = len(list(map(str, input().split())))

print(strs)
