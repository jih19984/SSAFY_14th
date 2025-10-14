# 문제
"""
비밀번호는 N개의 공백으로 구분된 정수
- 루프 안에 코드를 작성 (암호화 방식)
- 앨리스는 시작점이 몇인지 알려준다
- 그러나 해커는 암화화 쳬계를 알아냈지만 시작점을 모른다
- 해커는 암호화된 메시지를 2개 가지고 있음.
- 암호화된 메시지 두 개가 같은 비밀번호인지 파악하는 것이 출력값

input
- 비밀번호의 정수 개수 (1e5 이하)
- 2번째 줄: 첫번째 인코딩된 메시지의 정수에 해당하는 양의 정수들
- 3번째 줄: 두번째 인코딩된 메시지의 정수에 해당하는 양의 정수들

output
YES or NO
"""

# 풀이 방법
"""
암호화된 메시지 2개가 같은지 어떻게 확인할 것인가?

시도 1
deque 자료구조를 이용해 rotate 메서드로 1칸씩 회전하자
시간초과남 -> O(N^2) = for문 O(N) * rotate 메서드 O(N)

시도 2
암호 1개 뒤에 암호를 붙인 다음
2번째 암호가 안에 있는지 확인하자!
-> 멤버십 연산자는 리스트보다 문자열에서 매우 빠른 속도를 가지므로 문자열로 변환!!!!
"""

import sys

input = sys.stdin.readline

N = int(input())

pw1 = list(map(int, input().split()))
pw2 = list(map(int, input().split()))

# 구분자를 사용하여 문자열 변환 (중요!)
str1 = ' '.join(map(str, pw1))
str2 = ' '.join(map(str, pw2 + pw2))

if str1 in str2:
    print("YES")
else:
    print("NO")

