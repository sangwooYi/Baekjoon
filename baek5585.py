N = int(input())

rest_money = 1000-N
cnt = 0
while rest_money > 0:
    if rest_money >= 500:
        cnt += (rest_money // 500)
        rest_money %= 500
    elif rest_money >= 100:
        cnt += (rest_money // 100)
        rest_money %= 100
    elif rest_money >= 50:
        cnt += (rest_money // 50)
        rest_money %= 50
    elif rest_money >= 10:
        cnt += (rest_money // 10)
        rest_money %= 10
    elif rest_money >= 5:
        cnt += (rest_money // 5)
        rest_money %= 5
    else:
        cnt += rest_money 
        rest_money %= 1
print(cnt)