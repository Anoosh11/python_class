import re

person_data=[]

def show_menu():
    print("menu")
    print("1)Add person")
    print("2)find person by national code")
    print("3)show person list")
    print("0)exit")

    option =int(input("enter your choice:"))
    print("_"*40)
    return option

def name_checker(name):
    if re.match(r"^[a-z\s]{3,30}$",name,re.I):
        return True
    else:
        print("Error: invalid name!!!")
        return False

def family_checker(family):
    if re.match(r"^[a-z\s]{3,30}$",family,re.I):
        return True
    else:
        print("Error: invalid family!!!")
        return False

def email_checker(email):
    if re.match(r"^[a-z][a-z0-9._\s]{3,50}@(gmail|msn|yahoo)[.]com$",email,re.I):
        return True
    else:
        print("Error:invalid email!!!")
        return False

def mobile_checker(mobile):
    if re.match(r"^(09[0-9]{9}|989[0-9]{9})$",mobile):
        return True
    else:
        print("Error:invalid mobile!!!")
        return False

def national_code_checker(national_code):
    if re.match(r"^(\d{10}|\d{3}_{6}\d_\d)$",national_code):
        return True
    else:
        print("Error:invalid national code!!!")
        return False

def get_data():
    name=input("enter your name:")
    family=input("enter your family:")
    email=input("enter your email:")
    mobile=input("enter your mobile:")
    national_code=input("enter your national code:")
    if name_checker(name) and family_checker(family) and email_checker(email)and mobile_checker(mobile) and national_code_checker(national_code):
        person={"name":name,"family":family,"email":email,"mobile":mobile,"national_code":national_code}
        print("data added successfully")
    return person


def national_code_searcher():
    national_code_finder=input("enter your national code to search:")
    for person in person_data:
        if national_code_finder == person["national_code"]:
            print("national code found")
        else:
            print("national code not found")


def show_list():
    for person in person_data:
        print("show_list")
        print("name:",person["name"],"family:",person["family"],"email:",person["email"],"mobile:",person["mobile"],"national code:",person["national_code"])


