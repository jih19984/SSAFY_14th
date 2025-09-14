# 문제
""" 
문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 
만약 연결에 의해 또 반복문자가 생기면 이 부분을 다시 지운다.
최종적으로 남게되는 문자열의 길이를 출력하시오.
"""

T = int(input())

for tc in range(1, T+1):
    top = -1
    s = input()
    stack =[0] * 1000

    for ch in s:
        if top >= 0 and stack[top] == ch:
            top -= 1

        else:
            top += 1
            stack[top]=ch
    print(f"#{tc} {top + 1}")