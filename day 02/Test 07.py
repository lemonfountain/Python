# 排版練習兒 02-format
name1, name2, name3 = 'Jhon', 'Helen', 'Jo'
score1, score2, score3 = 90, 100, 45

print('name = {} score = {}'.format(name1, score1))  # format 後免可以有很多資訊
print('name = {1} score = {0}'.format(name1, score1))  # format 後免可以有很多資訊
print('name = {0} score = {1}'.format(name1, score1))
print('name = {0} score = {1}'.format(name1, score1, name2, score2))  # format 後免可以有很多資訊



cash = 1234567890

print('cash = {0:,}'.format(cash))  # {0} 第一位預設 ; {} 預設為0

# EX 01
# 請輸出到小數點第二位並帶千分號 -> 1,234,567,890.54
amount = 1234567890.54321
#print(amount, type(amount))
#amount = float(amount)
print('amount = {0:,.2f}'.format(amount))

# 老師解題
print("amount = {:,}".format(float('%.2f' % amount)))
