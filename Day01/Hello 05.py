import math
# 數學相關應用

x = 9
y = math.sqrt(x)  # 開根號
print(y)

z = math.pow(y, 2)  # 次方ㄝ等同**2

# Q1: A(5, 3) B(-6, 8), 求兩點間距離

x1, y1 = 5, 3
x2, y2 = -6, 8

dx = math.pow(x1 - x2, 2)
dy = math.pow(y1 - y2, 2)
d = math.sqrt(dx + dy)
print("%.1f" % d)
