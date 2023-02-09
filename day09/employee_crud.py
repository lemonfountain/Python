import sqlite3
# employee 資料表 crud
# crud = create, read, update, delete


# 建立一筆員工紀錄
def create_employee(employee_name, employee_salary):
    # 新增的sql 語句
    sql = 'insert into employee(employee_name, employee_salary) values(?, ?)'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    args = [employee_name, employee_salary]   # 建立一個list 存放要新增的資料
    cursor = cursor.execute(sql, args)
    print('新增筆數:{}'.format(cursor.rowcount))  # 因著語句所影響想的資料筆數
    print('最新 id 值:{}'.format(cursor.lasrrowid))
    conn.commit()
    conn.close()  # 一定要close



