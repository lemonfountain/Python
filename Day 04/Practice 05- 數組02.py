import random as r

# 數組練習- poker
poker = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'] * 4
print(poker)
print(len(poker))

# 洗牌 (交換位置)
poker[0], poker[1] = poker[1], poker[0]  # print 從['A', '2'] -> ['2', 'A']
print(poker)

# 用 random 隨機洗牌100次  print: 隨機:['9', 'J', '10', 'K', '4', 'Q', 'A', '9', '3', '2', .......
for i in range(0, 100):
    first = r.randint(0, 51)
    second = r.randint(0, 51)
    poker[first], poker[second] = poker[second], poker[first]
print(poker)

# 取兩張牌  總排數52張,取兩張便50(len)
card_one = poker.pop()  # 取得最後⼀個元素並刪除; 取牌後刪掉,所以會少
card_two = poker.pop()
print(card_one, card_two)
print(poker)
print(len(poker))
