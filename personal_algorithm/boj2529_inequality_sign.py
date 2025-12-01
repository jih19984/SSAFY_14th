# 문제
"""
두 종류의 부등호 기호 "<" ">"가 k개 나열된
순서열 A가 존재

우리는 이 부등호 기호 앞뒤에 서로 다른 한 자릿수 숫자를 넣어서
모든 부등호 관계를 만족시키고자한다.

- 부등호 앞에 넣을 수 있는 숫자는 0~9
- 숫자는 모두 달라야 한다.

이 상황에서 부등호를 모두 제거한뒤 모든 숫자를 이어 붙인 수를
부등호 관계를 만족시키는 정수라고 한다.

-> 이 때 정수에서 첫 자리가 0인 경우도 정수에 포함되어야 한다. (출력 정수는 하나의 문자열)

k개의 부등호 순서를 만족하는 k+1자리의 정수 중 최댓값과 최솟값을 찾으시오.
(k의 범위는 2이상 9이하)

예시
<input>
9
> < < < > > > < <

<output>
9567843012
1023765489
"""

# 풀이 방법
"""
어떻게 접근할 것인가?

- 모든 숫자가 겹치지 않아야 하므로 visited 배열 생성
- 새로 추가될 숫자가 이전의 숫자와 비교되어야하므로, 이전 숫자를 인자로 넘겨준다.
- 인덱스는 숫자의 개수로 설정
"""

import sys
input = sys.stdin.readline 

def find_int(idx, strs, prev_strs):

    global max_num, min_num

    if idx == N + 1:
        # 모든 숫자를 선택했으면 최대/최소 비교
        # 1. 일단 빈 값이면 초기값 무조건 할당
        if max_num == "":
            max_num = strs
            min_num = strs
        # 2. 이후 최소, 최대 값 갱신
        else:
            if strs > max_num:
                max_num = strs
            if strs < min_num:
                min_num = strs
        return
    
    for num in range(10):
        if not visited[num]:
            if idx == 0 or (inequality_signs[idx-1] == '<' and prev_strs < num) or (inequality_signs[idx-1] == '>' and prev_strs > num):
                visited[num] = True
                find_int(idx+1, strs + str(num), num)
                visited[num] = False


N = int(input())
inequality_signs = input().split()
max_num, min_num = "", ""
visited = [False] * 10
find_int(0, "", -1)

print(max_num)
print(min_num)