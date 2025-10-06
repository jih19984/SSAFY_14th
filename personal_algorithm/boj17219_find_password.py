# 문제
"""
눈을 감고 키보드를 막쳐서 나온 두 문자열에서 공통으로 존재하는
가장 긴 부분 문자열을 비밀번호로 하기로 결정

메모장에서 비밀번호를 찾아라!
첫째 줄에 사이트의 주소의 수: N 와 비밀번호를 찾여르녀는 사이트의 주소 수: M
둘째 줄부터 N개의 줄에 걸쳐 사이트 주소와 비밀번호가 공백으로 주어진다.

사이트 주소
- 알파벳 소문자, 대문자, '-', '.'으로 이루어지며 중복되지 않는다.

비밀번호
- 모두 대문자로 이루어짐
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

site_pw = {}

for _ in range(N):
    site, pw = input().strip().split()
    site_pw[site] = pw

for _ in range(M):
    find_pw = input().strip()
    print(site_pw[find_pw])