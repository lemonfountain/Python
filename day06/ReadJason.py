import json
json_str = '{"name:"Jhon", "salary": 45000, "age": 28}'
# 轉dict數組
emp = json.loads(json_str)  # 將json string 轉為 dict 數組
print(emp, type(emp))

#改變薪資
emp['salary'] = emp['salary'] * 1.2
print(emp)
print("-------------------------------------------")

# 傳送給原端

json_str = json.dumps(emp)   # 將dict  轉為 json string
print(json_str, type(json_str))
 