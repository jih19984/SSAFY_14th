# 문제
"""
티셔츠 한 장과 펜 한 자루가 포함된 웰컴키트를 나눠줄 예정
티셔츠: S, M, L, XL, XXL, XXXL
펜: 한종류

- 티셔츠와 펜은 각각 T장 또는 P자루씩 묶음으로 구매 가능
- 티셔츠는 남아도 되지만, 펜은 남거나 부족하면 안됨.

-> T셔츠는 최소 몇 묶음, 펜은 최대 몇 묶음 주문할 수 있고, 그 때 펜을 한자루씩 몇 개 주문하는지 구하시오.

입력:
- 참가자 수: N
- 둘째 줄에 티셔츠 사이즈별 신청자의 수 S, M, L, XL, XXL, XXXL이 공백으로 구분되어 주어짐
- 티셔츠와 펜의 묶음 수를 의미하는 정수 T와 P가 공백으로 주어짐

출력:
- 티셔츠를 T장씩 최소 몇 묶음
- 펜을 P자루씩 최대 몇 묶음, 그 때 펜을 한 자루씩 몇 개 주문하는지 구하는지 출력
"""

import sys
input = sys.stdin.readline

N = int(input().strip())
t_list = list(map(int, input().split()))
T, P = map(int, input().split())


t_set = 0 # 필요 티셔츠 묶음 수

# 티셔츠 최소 몇 묶음 필요한가?
# 각 사이즈 별 티셔츠의 개수가 묶음의 개수보다 작다면 +1 묶음
# 크다면 묶음 수로 나눈 몫 + 1

for i in range(len(t_list)):
    if t_list[i] == 0:
        continue
    if t_list[i] < T:
        t_set += 1
    else:
        if t_list[i] % T != 0:
            t_set += (t_list[i] // T) + 1
        else:
            t_set += (t_list[i] // T)

print(f"{t_set}")
print(f"{N//P} {N%P}")