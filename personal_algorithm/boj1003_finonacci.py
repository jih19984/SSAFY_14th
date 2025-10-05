# 문제
"""
fibonacci(N)을 호출했을 때 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.
fibonacci 수열이란?
이전 2개의 요소의 합이 현재 요소가 되는 수열
"""

# 풀이 방법
"""
그냥 피보나치 함수로 돌리면 시간제한이 0.25초이기 때문에 무조건 터짐
규칙을 찾아야 한다 !
0 1 1 2 3 5 8 

n = 0 -> 1 0
n = 1 -> 0 1
n = 2 -> 1 1
n = 3 -> 1 2
n = 4 -> 2 3

즉 n = 3 부터 이전 0과 1의 개수의 개수를 더한 값이 결과가 된다. 
"""
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    if N == 0:
        print(f"{1} {0}")
    elif N == 1:
        print(f"{0} {1}")

    else:
        lst = [[1, 0], [0, 1]]

        for i in range(N-1):
            lst.append([lst[i][0] + lst[i+1][0],  lst[i][1]+lst[i+1][1]])

        print(*lst[len(lst)-1])
