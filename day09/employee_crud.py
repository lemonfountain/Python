import sqlite3
# employee 資料表 crud
# crud = create, read, update, delete


# 建立單筆員工紀錄
def create_employee(employee_name, employee_salary):
    # 新增的sql 語句
    sql = 'insert into employee(employee_name, employee_salary) values(?, ?)'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    args = [employee_name, employee_salary]   # 建立一個list 存放要新增的資料
    cursor = cursor.execute(sql, args)
    print('新增筆數:{}'.format(cursor.rowcount))  # 因著語句所影響想的資料筆數
    print('最新 id 值:{}'.format(cursor.lastrowid))  # create 單筆資料時用
    conn.commit()
    conn.close()  # 一定要close

# 建立多筆資料
def create_many_employee(employees):
    sql = 'insert into employee(employee_name, employee_salary) values(?, ?)'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor = cursor.executemany(sql, employees)   # 要用 .executemany 因為此employees 是一個這樣的數組 [('Jhon', 35000), ('Mary', 42000), ('Bob', 68000) ....]
    conn.commit()
    conn.close()

# 查詢 多筆 資料
def find_all_employee():
    # 查詢語句
    sql = 'select id, employee_name, employee_salary, create_time from employee'  # 不要用*，要全部資料列出來
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    employees = cursor.execute(sql).fetchall()
    print('%2s %-7s %8s %24s' % ('Id', 'Name', 'Salary($)', 'Create Time'))
    print('---------------------------------------------')
    for emp in employees:  # 逐筆印出
        print('%2s %-7s %8s %24s' % (emp[0], emp[1], '{:,}'.format(emp[2]), emp[3]))
    print('---------------------------------------------')
    conn.close()


# 查詢 單筆 資料
def find_one_employee(id):
    sql = 'select id, employee_name, employee_salary, create_time from employee where id = ?'  # 這邊用sql 指令語法
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    employee = cursor.execute(sql, [id]).fetchone()
    if employee is None:
        print("查無資料")
    else:
        print(employee)
    conn.close()

def get_sum_avg_employee_salary():
    sql = 'select sum(employee_salary), avg(employee_salary) from employee'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    data = cursor.execute(sql).fetchone()
    print(data, type(data))  # <class 'tuple'>
    print('總薪資:{:,} 平均薪資:{:,}'.format(data[0], data[1]))
    conn.commit()
    conn.close()

# 修改資料
def update_employee(employee_name, employee_salary, id):
    sql = 'update employee set employee_name =?, employee_salary=? where  id=?'
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    args = [employee_name, employee_salary, id]
    cursor = cursor.execute(sql, args)
    print('資料更新筆數: {}'.format(cursor.rowcount))
    conn.commit()
    conn.close()

# 刪除資料
def delete_employee(id):
    sql = 'delete from employee where id =?'  # delete 一定要加 from; 其他的不用
    conn = sqlite3.connect('demo.db')
    cursor = conn.cursor()
    cursor = cursor.execute(sql, [id])
    print('資料刪除筆數: {}'.format(cursor.rowcount))
    conn.commit()
    conn.close()
