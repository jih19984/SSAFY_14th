# 문제
"""
거스름돈 주기
쿼터: $0.25 -> 25
다임: $0.10 -> 10
니켈: $0.05 -> 5
페니: $0.01 -> 1

거스름 돈을 주기 위한 각 동전의 개수를 출력하시오.

조건
- 거스름 돈은 항상 $5.00 이하
- 손님이 받는 동전의 개수는 최소화
"""

T = int(input())

for tc in range(1, T+1):
    money = int(input())
    qt = 0
    di = 0
    ni = 0
    pe = 0
    while True:
        if money >= 25:
            money -= 25
            qt += 1
        else:
            break

    while True:
        if money >= 10:
            money -= 10
            di += 1
        else:
            break


    while True:
        if money >= 5:
            money -= 5
            ni += 1
        else:
            break


    while True:
        if money >= 1:
            money -= 1
            pe += 1
        else:
            break

    print(f"{qt} {di} {ni} {pe}")