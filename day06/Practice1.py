import re
# 資料讀取
def get_employees(filename, colume1='name', column2='salary', column3=None):
    file = open(filename, 'r', encoding='UTF-8')
    rows = file.readlines()
    # print(rows)
    # 資料整理
    '''
    For example:
    employees = 
    [
        {"name": "John", "salary": 45000},
        {"name": "Mary", "salary": 85000},
        {"name": "傑克", "salary": 75000},
        {"name": "蘿絲", "salary": 60000},
        ...
    ]
    '''
    employees = []  # 建立新的list
    for i, row in enumerate(rows):  # 假設一個 i
        if i == 0:  # 要跳掉第一行
            continue
        if len(row.strip()) == 0:
            continue
        # print(row)
        data = re.split(' |, |,|#', row)  # 防止有空白或逗號或#符號,要濾掉
        # print(data)
        # --------------------------------------
        emp = {}  # 建立一個 dict 數組
        emp.setdefault(colume1, data[0].strip())  # .strip() 去空白
        emp.setdefault(column2, int(data[1]))  # .strip() 去空白
        # 是否有第三個欄位? column3
        if column3 is not None:  #假設有第三欄
            emp.setdefault(column3, int(data[2].strip()))

        # --------------------------------------
        employees.append(emp)

    return employees