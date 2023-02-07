import random as r
# 數組(同陣列) set() 元組不可重複串列列表
nums = set()
nums.add(10)
nums.add(10)
nums.add(9)
print(nums, len(nums))

# 樂透 539, 1~39取出不重複的5個數字
# 請選出電腦選號程式
lotto = set()
while len(lotto) < 5:  # < 5 : 不重複的5個
    lotto.add(r.randint(1, 39))
print(lotto, len(lotto))  #{ 6, 10, 22, 26, 30} 5

# set()  沒有index
# 所以要轉成list
lotto = list(lotto)
lotto = tuple(lotto)
print(lotto)  # print : (6, 10, 22, 26, 30)
print(lotto[0])
print(lotto[0])
# 改成read only 正列
lotto = tuple(lotto)
print(lotto)  # print : (6, 10, 22, 26, 30)
print(lotto[0])
print(lotto[0])
