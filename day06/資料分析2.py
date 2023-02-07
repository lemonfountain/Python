import matplotlib.pyplot as plt
import statistics as stat
from day06.Practice1 import get_employees

if __name__ == '__main__':
    employees = get_employees('salary_age.txt', column3='age')
    print(employees)
    # 繪製薪資與年齡的摺線圖
    names = [emp['name'] for emp in employees]
    salary = [emp['salary']//1000 for emp in employees]  # 將薪資除以1000
    age = [emp['age'] for emp in employees]
    print(names)
    print(salary)
    print(age)
    # 計算變異係數CV
    salary_cv = stat.stdev(salary) / stat.mean(salary)
    age_cv = stat.stdev(age) / stat.mean(age)


    plt.rcParams['font.sans-serif'] = ['Microsoft JhengHei']
    plt.rcParams['axes.unicode_minus'] = False
    plt.plot(names, salary, marker="o", label="薪資(k) CV:{0:.2F}% 平均:{1:,.1f}K".format(salary_cv*100, stat.mean(salary)))
    plt.plot(names, age, marker="o", label="年齡CV:{0:.2F}% 平均:{1:,.1f}".format(age_cv*100, stat.mean(age)))
    plt.legend()
    plt.grid(True)
    plt.ylabel("年齡/薪資(k)")  # Y軸標題
    plt.xlabel("姓名")  # X軸標題
    plt.title("員工資料統計")
    plt.show()
