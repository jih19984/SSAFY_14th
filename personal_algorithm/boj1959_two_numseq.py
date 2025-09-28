# 문제
"""
N개의 숫자로 구성된 숫자열 A와
M개의 숫자로 구성된 숫자열 B가 있다.

숫자열을 자유롭게 움직여서 서로 마주보는 위치를 변경할 수 있을 때
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구해라.
"""

# 풀이 방법
"""
긴 숫자열은 가만히 두고 더 작은 숫자열을 움직이는 방식으로 해보자
같은 길이의 리스트 간의 곱은 어떻게 구할 것인가? -> zip을 쓰자
"""

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    seq_a = list(map(int, input().split()))
    seq_b = list(map(int, input().split()))
    result = 0

    if N >= M:
        for i in range(N-M+1):
            div_seq_a = seq_a[i:i+M] 
            product = [a * b for a, b in zip(div_seq_a, seq_b)]
            result = max(sum(product), result)
    elif N < M:
        for j in range(M-N+1):
            div_seq_b = seq_b[j:j+N]
            product = [a * b for a, b in zip(div_seq_b, seq_a)]
            result = max(sum(product), result)

    print(f'#{tc} {result}') 
            