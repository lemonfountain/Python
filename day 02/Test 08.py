#if- else 練習
# 使用者輸入一個數，且能判斷機/偶數

num = int(input('請輸入數字:'))
# Answer 01
if num % 2 == 0:
        print(num, '是偶數')
else:
        print((num, "奇數"))


# Answer 2-------------
is_odd = num % 2 == 0
print(is_odd, type(is_odd))
if is_odd:
    print(num, "是偶數")
else:
    print(num, "是奇數")

# Answer 03-------------

print(num, '是偶數' if is_odd else '是奇數')
