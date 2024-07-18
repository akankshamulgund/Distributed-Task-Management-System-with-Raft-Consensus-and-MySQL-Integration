import json

exmployee = '{"id": "09", "name": "James"}'
print(type(exmployee))

# now json

employee_dict = json.loads(exmployee)
print(employee_dict)
print(type(employee_dict))