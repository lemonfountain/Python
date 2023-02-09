from day09.employee_crud import  create_employee, create_many_employee

# 建立資料
if __name__ == "__main__":
    # create_employee('Jhon', 45000)
    # create_employee('Mary', 55000)
    # 新增多筆資料
    employees = [
        ('Helen', 72000),
        ('Alen', 120000),
        ('Bob', 80000)
    ]
    create_many_employee(employees)
