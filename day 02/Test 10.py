words = '小明本新$65000,今年公司發放6個月,試問小明的年終'
print(words[5:10])  # print 65000
print(words[words.find('$')+1:words.find(',')])  # 從五開始，到六開始找(+1，會找到6這個數字)找到10的數字，不包含10
print(words[words.find('發放')+2:words.find('個月')])

# -----------------------------------------
salary = int(words[words.find('$')+1:words.find(',')])
month = int(words[words.find('發放')+2:words.find('個月')])
print(salary*month)


