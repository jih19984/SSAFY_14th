# 문제
"""
start: 16:30
end: 17:30

학생들이 되도록이면 많은 단어를 읽을 수 있도록 하고자 한다.
가르칠 수 있는 글자: K개
학생들은 K개의 글자로만 이루어진 단어만을 읽을 수 있다.

선생님은 어떤 K개의 글자를 가르쳐야 학생들이 읽을 수 있는 단어의 개수가 최대인지 찾고자 한다.

모든 단어는 anta로 시작해 tica로 끝난다.
이 언어에는 단어가 N개 밖에 없다.

N: 1 <= N <= 50
K: 0 <= K <= 26
8 <= 단어 길이 <= 15

! 모든 단어는 중복되지 않는다 !

<input>
N
K
N줄에 걸쳐 남극 언어의 단어
"""

# 풀이 방법
"""
초기 문자 종류 5개
anta tica -> a, c, i, n, t

글자를 3개로 추가로 배울 수 있다!

1. anta와 tica를 제외하고 남은 문자열을 찾는다.
2. 이 남은 문자열에서 K-5를 한 뒤 고를 수 있는 문자열의 경우의 수를 모두 고려
"""
import sys
from itertools import combinations
input = sys.stdin.readline

N, K = map(int, input().split())
words = [set(input().strip()) for _ in range(N)]

# K < 5일 때 문자 가르치기 부라ㄱ능
if K < 5:
    print(0)

# 알파벳의 개수는 총 26개이므로 다 가르치면 N개의 단어를 모두 읽기 가능
elif K == 26:
    print(N)

else:
    base_alphabet = set('acint')
    extra = set()

    # 필요한 추가 문자들만 추출
    for word in words:
        extra = extra | word - base_alphabet

    if len(extra) <= K - 5:
        print(N)

    else:
        max_cnt = 0
        for combination in combinations(extra, K-5):
            learned_alphabet = base_alphabet | set(combination)
            cnt = 0
            for word in words:
                # 만약에 단어의 알파벳 수가 현재 배운 알파벳 수보다 작다면
                # 당연히 읽을 수 있으므로 cnt + 1
                if word <= learned_alphabet:
                    cnt += 1
            max_cnt = max(max_cnt, cnt)
        print(max_cnt)
    


