# 문제
"""
N개의 수가 주어졌을 때,
이를 오름차순으로 정렬하시오.

오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
"""

# 풀이 방법
"""
일반 정렬로 문제를 풀면 반드시 시간초과가 발생
sort() -> O(nlogn) -> 천만의 경우 2억 ~ 3억 연산 시행으로 시간 초과 확률 up
따라서 계수 정렬을 사용해야 한다.

sys.stdout.write을 쓰는 이유
일반적으로 print함수는 3단계를 거친다.
1. 문자열 변환
2. 줄바꿈 처리
3. 즉시 화면 출력

그러나 sys.stdout.write은 즉시 화면에 문자열을 출력 버퍼에 밀어 넣음.
"""
import sys
input = sys.stdin.readline

N = int(input())
count = [0] * 10001

for _ in range(N):
    num = int(input())
    count[num] += 1

for i in range(1, 10001):
    while count[i] > 0:
        print(i)
        count[i] -= 1
