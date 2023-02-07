# 求小於10000的最大質數
for num in range(10000, 2, -1):  # 從10000往前跑(-1) 到 2
    is_prime = True  # 假設 num 是質數
    for i in range(2, num // 2 + 1):
        if num % i == 0:
            is_prime = False
            break

    if is_prime:
        print('{} 是質數'.format(num))
        break
