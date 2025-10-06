# 문제
"""
N: 포켓몬의 개수
M: 맞춰야 하는 문제의 개수

<input>
N, M
N개의 줄에 걸쳐 포켓못이름이 주어진다. (포켓몬이 입력되는 순서가 포켓몬 번호)
M개의 줄에 걸쳐 숫자 또는 포켓몬 이름이 주어진다.

<output>
숫자인 경우 포켓못 이름을
포켓몬 이름일 경우 숫자를 출력하시오.
"""

# 풀이방법
"""
그냥 리스트로 하면 index가 O(n)이기 때문에 무조건 시간 터짐.
"""

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

pocket_lst = [0] * (N+1)
name_to_num = {}

for i in range(1, N+1):
    name = input().strip()
    pocket_lst[i] = name
    name_to_num[name] = i

for _ in range(M):
    quiz = input().strip()
    if quiz.isdigit():
        print(pocket_lst[int(quiz)])
    else:
        print(name_to_num[quiz])

