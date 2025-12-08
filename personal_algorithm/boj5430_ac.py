# 문제
"""
start 16:20
end 16:40

AC란 정수 배열에 연산을 하기 위해 만든 연산자

두가지 함수 R과 D가 존재.

R: 배열에 있는 수의 순서 뒤집기
D: 첫 번째 수를 버리기

배열이 비어있는데 D를 사용한 경우 에러 발생

<입력>
테스트 케이스 개수: T
1 <= p <= 100,000
배열에 들어있는 수 개수: n (0 <= n <= 100,000)
배열에 들어있는 정수가 주어짐.

전체 테스트 케이스에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않음.
"""

# 풀이 방법
"""
모든 수를 계속 뒤집을 필요가 있는가? -> 그렇지 않다.
지금 고려해야 하는 건 D의 위치!
D앞에 R이 몇 번 있는지에 따라 맨 앞의 값을 뺄지, 맨 뒤의 값을 뺄지 결정
"""

from collections import deque
import sys
input = sys.stdin.readline

""" 1. 입력 정의 """

T = int(input())

for _ in range(T):
    RD = input().strip()
    n = int(input())
    arr_input = input().strip()

    """ 2. input이 리스트 형태로 들어옴에 유의 """
    if arr_input == "[]":
        arr = deque()
    else:
            arr = deque(map(int, arr_input[1:-1].split(',')))

    """ 3. error 상태, reverse 상태 체크 변수 선언 """
    is_reversed = False
    error = False

    """ 4. reverse 상태를 계속 체크해주면서, D 실행 """
    for rd in RD:
        if rd == 'R':
            is_reversed = not is_reversed
        else:
            if not arr:
                 error = True
                 break
            
            if is_reversed:
                 arr.pop()
            else:
                 arr.popleft()

    """ 5. 최종 결과 및 error 출력 """
    if error:
         print("error")
    else:
         if is_reversed:
              arr.reverse()
         print('[' + ','.join(map(str, arr)) + ']')


    

