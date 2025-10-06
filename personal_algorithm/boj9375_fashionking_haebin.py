# 문제
"""
해빈이는 한 번 입었던 옷들의 조합을 절대 다시 입지 않는다.

첫째 줄에 테스트 케이스가 주어진다.
첫째줄에 의상의 수 n이 주어진다. (n은 30이하의 자연수)
다음 n개에는 해빈이가 가진 의상의 이름과 의상의 종류가 공백으로 구분된다.

각 테스트 케이스에서 해빈이가 알몸이 아닌 상태로 의상을 입을 수 있는 경우의 수를 출력하시오.
"""

# 풀이 방법
"""
2번째 요소만 확인하면 Ok
각 의상의 종류만큼 개수를 구한 후 (a+1) * (b+1) - 1
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    result = 1
    n = int(input())

    tmp_lst = []
    for _ in range(n):
        name, categories = input().strip().split()
        tmp_lst.append(categories)
    for category in set(tmp_lst):
        result *= (tmp_lst.count(category)+1)
    print(f"{result-1}")

