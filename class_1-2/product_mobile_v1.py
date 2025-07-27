import re

mobile_list=[]

def show_menu():
    print("menu")
    print("1)Add mobile:")
    print("2)find by code")
    print("3)find by price")
    print("4)show list")
    print("0)exit")

    option = int(input("enter your choice: "))
    print("_"*40)
    return option

def code_checker(code):
    if re.match(r"^[a-z0-9]{3,30}$",code,re.I):
        return True
    else:
        return False

code_list = []
def code_same_checker(code):
    while True:
        code_list.append(code)
        if code == "exit":
            break
l = []
for i in range(len(code_list)):
    if code_list[i] in l:
        break
    else:
        l.append(code_list[i])


def name_checker(name):
    if re.match(r"^[a-z0-9]{3,30}$",name,re.I):
        return True
    else:
        return False

def brand_checker(brand):
    brand_list=["samsung".lower(),"iphone".lower(),"nokia".lower()]
    if brand in brand_list:
        return True
    else:
        return False

def price_checker(price):
    if 1000<=price<=2000:
        return True
    else:
        return False

def get_data():
    code=input("enter your mobile code: ")
    name=input("enter your mobile name: ")
    brand=input("enter your mobile brand: ").lower()
    price=int(input("enter your mobile price: "))
    if code_checker(code) and name_checker(name) and brand_checker(brand) and price_checker(price):
        mobile={"code":code,"name":name,"brand":brand,"price":price,}
        mobile_list.append(mobile)

def code_finder():
    code_fnd=input("enter your code to find:")
    for mobile in mobile_list:
        if mobile["code"] == code_fnd:
             print("mobile found")
        else:
            print("code not found")



def price_finder():
    price_fnd=input("enter your price to find:")
    for mobile in mobile_list:
        if mobile["price"] == price_fnd:
            print("price found")
        else:
            print("price not found")

def show_list():
    print("list")
    for mobile in mobile_list:
        print("code is:",mobile["code"],"name is:",mobile["name"],"brand is:",mobile["brand"],"price is:",mobile["price"])

