import keyword
#  保留字
print(keyword.kwlist)


# 變數的覆值
# EX 01
a = 100
b = 100
c = 100  # or a = b = c = 100
#EX 02
age, name = 18, "Jhon", True
print(age, type(age))
print(name, type(name))
print(ok, type(ok))

# 刪除變數
del age
print(age)  #錯誤示範，刪除不能再用