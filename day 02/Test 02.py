#資料轉型(變態 = 改變資料型態)
#EX01
# str -> int
# str _> float
# int -> str etc...
chinese = '100'  #str
english = 80  #int
math = '70.5'  #str
#開始轉型
chinese = int(chinese)
math = float(math)

total = chinese + english + math
print(total)
