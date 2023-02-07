#隨機數
import random as r


num = r.randint(1, 5)  # 此 num 包含隨機數 1 和 5
print(num)
num = r.randrange(1, 5)  # 此 num 不包含隨機數 1 和 5
print(num)

# 樂透電腦選號-三星彩
# (0-9) 選三個可重複的數字
n1 = r.randint(0, 9)
n2 = r.randint(0, 9)
n3 = r.randint(0, 9)
# 以下為不同print法
print('電腦選號:%d%d%d' % (n1, n2, n3))
print('電腦選號: ', end=' ')
print(n1, end=' ')  # end 是結尾符號 ; sep 是分開符號
print(n2, end=' ')
print(n3, end=' ')
print(n3)
print('%02d' % n1, end=' ')


