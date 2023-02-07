# 字串的處理 str
words = 'she sell sea shell on the sea shore'
print('字數:', len(words))  # len() 字長function
print(words[2:10])
print('有幾個s:', words.count('s'))  # words.count() 屬字數function
print('words中是否有包含sea 這個字:', words.find('sea'))  # words.find()  找字function
print('words中是否有包含sea 這個字:', words.find('sky'))
print('words中是否有包含sea 這個字:', words.find('sea'), ' 有' if words.find('sea') >= 0 else '無')
# words 有幾個字
amount = len(words.split())  # split 切割字串 (預設就是以""切割)
print(amount)
# 取的每一個字
word = words.split()
print(words)
print(word)
print(word[0])  #取第一個字
print(word[1])  #取第2個字
print(word[-1])  #取y最後一個字
print(word, type(words))
print(words, type(words))





