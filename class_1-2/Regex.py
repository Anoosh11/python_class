import re

national_ID=input("Enter National ID: ")
print(re.match(r"^(\d{10}|\d{3}-/d{6}-\d)$",national_ID))

address=input("Enter address: ")
print(re.match(r"^[a-zا-ی0-9.,-]{30}$",address,re.I))

plate=input("Enter plate: ")
print(re.match(r"^\d{2}[a-z]{1}\d{3}-iran\d{2}$",plate,re.I))

email=input("Enter email: ")
print(re.match(r"^a[0-9.]z{2,50}@(gmail|yahoo|msn)$",email,re.I))

moblie=input("Enter moblie: ")
print(re.match(r"^(09[0-9]{9}|989[0-9]{9})$",moblie,re.I))

age=input("Enter age: ")
print(re.match(r"^[0-150]{1,3}$",age))


