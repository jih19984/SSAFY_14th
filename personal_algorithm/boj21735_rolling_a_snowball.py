# 문제
"""
앞마당의 길이가 N
위치가 1부터 N까지만 눈이 쌓여있다.
대회 규칙은 앞마당에서 M초 동안 눈덩이를 굴려 눈사람을 만드는 것이다.

눈덩이의 시작 크기: 1
눈덩이의 시작 위치: 0

눈덩이를 굴리는 방법
- 눈덩이를 현재 위치 +1칸으로 굴린다.
- 눈덩이를 현재 위치 +2칸으로 던진다. 눈던이가 착지하며 크기느 원래 크기의 절반으로 줄어듦.
그리고 현재 칸의 위치가 i라하면, a_i+2 만큼 눈덩이 크기가 늘어난다. 이때 소수점은 절사. 눈덩이를 던져 크기가 0이 되어도
눈덩이는 사라지지 않음.

눈덩이가 앞마당의 끝에 도달한 경우 남은 시간과 관계없이 눈덩이 굴리기는 끝이 난다.
대회 시간 내에 가장 크게 만들 수 있는 눈덩이의 크기를 구하는 프로그램을 작성하자!
"""

# 풀이 방법
"""
<input>
앞마당의 길이 N, 대회의 시간 M
길이가 N인 수열 a

<output>
대회 시간 내에 가장 크게 만들 수 있는 눈덩이의 크기
"""

import sys
input = sys.stdin.readline

def backtracking(idx, snowball_size, snow_time):
    global max_snowball_size

    # 앞마당 끝 도달 또는 시간 초과
    if idx >= N or snow_time >= M:
        max_snowball_size = max(max_snowball_size, snowball_size)
        return

    max_snowball_size = max(max_snowball_size, snowball_size)

    # 방법 1: +1칸 굴리기 (위치 idx → idx+1, 배열 a[idx]의 눈을 더함)
    if idx + 1 <= N:
        backtracking(idx + 1, snowball_size + a[idx], snow_time + 1)
    
    # 방법 2: +2칸 던지기 (위치 idx → idx+2, 배열 a[idx+1]의 눈을 더함)
    if idx + 2 <= N:
        backtracking(idx + 2, snowball_size // 2 + a[idx + 1], snow_time + 1)

N, M = map(int, input().split())
a = list(map(int, input().split()))
snowball_size = 1
max_snowball_size = 0
snow_time = 0

backtracking(0, snowball_size, snow_time)

print(max_snowball_size)

