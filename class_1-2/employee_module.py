import re

employee_list=[]

def show_menu():
    print("menu")
    print("1) Add employee")
    print("2) show employee list")
    print("3) exit")

    option=int(input("enter your choice:"))
    print("_"*40)
    return option

def name_checker(name):
    if re.match(r"^[a-z\s]{3,30}$",name,re.I):
        return True
    else:
        print("Error: invalid name!!!")
        return False

def family_checker(family):
    if re.match(r"^[a-z\s]{3,30}$",family, re.I):
        return True
    else:
        print("Error: invalid family!!!")
        return False

def age_checker(age):
    if 20<=age<=30:
        print("acceptable age")
        return True
    else:
        print("not acceptable age")
        return False

def get_data():
    name = input("enter your name:")
    family = input("enter your family:")
    age = int(input("enter your age:"))
    if name_checker(name) and family_checker(family) and age_checker(age):
        employee={"name":name,"family":family,"age":age}
        employee_list.append(employee)

def show_list():
    for employee in employee_list:
        print("employee list")
        print("employee name:",employee["name"],"employee family:",employee["family"],"employee age:",employee["age"])

