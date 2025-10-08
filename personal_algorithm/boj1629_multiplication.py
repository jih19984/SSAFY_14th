# 문제
"""
자연수 A를 B번 곱한 수를 알고 싶다.
단 구하려는 수가 매우 커질 수 있으므로, 이를 C로 나눈 나머지를 구하는 프로그램을 작성하시오.
A, B, C는 모두 2,147,483,647 이하의 자연수
A^B % 3 
"""

# 풀이 방법
"""
5 * 5 * 5 % 11 = 4

25를 11로 나눈 나머지 3
5를 11로 나눈 나머지 5

15 % 11 = 4

그냥 제곱을 해버리면 21억의 21억 제곱은 무조건 터짐..
모듈러 연산을 시행해야 한다!
(a x b) % c = ((a % c) x (b % c)) % c

(25 % 11) x (5 % 11) % 11 = 4

다시 정리하면
a * a * a * a가 있으면,
a * a, a * a
a, a, a, a
(((a % c) % c) * (a % c) % c)가 무한 반복
재귀로 계속 들어가는 구조 
언제까지? B가 1이 될 때까지. A를 C로 1번만 나눌때까지
"""

import sys
input = sys.stdin.readline

def modular(A, B, C):
    if B == 1:
        return A % C
    
    if B % 2 == 0:
        tmp = modular(A, B//2, C)
        return (tmp * tmp) % C
    
    else:
        tmp = modular(A, B//2, C)
        return (tmp * tmp * A) % C
    
A, B, C = map(int, input().split())

print(modular(A, B, C))
