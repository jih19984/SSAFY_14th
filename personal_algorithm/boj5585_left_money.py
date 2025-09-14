# 문제
"""
거스름 돈
500, 100, 50, 10, 5, 1
거스름돈의 개수가 가장 적게 잔돈을 준다.

1000엔을 1장 냈을 때, 받을 잔돈에 포함된 잔돈의 개수를 구하시오.
"""

money = 1000 - int(input())
cnt = 0
while True:
    if money >= 500:
        money -= 500
        cnt += 1
    else:
        break

while True:
    if money >= 100:
        money -= 100
        cnt += 1
    else:
        break

while True:
    if money >= 50:
        money -= 50
        cnt += 1
    else:
        break

while True:
    if money >= 10:
        money -= 10
        cnt += 1
    else:
        break

while True:
    if money >= 5:
        money -= 5
        cnt += 1
    else:
        break

while True:
    if money >= 1:
        money -= 1
        cnt += 1
    else:
        break

print(f"{cnt}")