import re
info_list=[]
while True:
    print(" Menu ")
    print("1) Add person")
    print("2) find person by national code")
    print("3) show person")
    print("4) exit")
    option=input("Enter option: ")
    print('*'*40)
    if option=="1":
        first_name=input("Enter first name: ")
        last_name=input("Enter last name: ")
        email=input("Enter email: ")
        mobile=input("Enter mobile: ")
        national_code=input("Enter National code: ")

        year=int(input("Enter year: "))
        month=int(input("Enter month: "))
        day=int(input("Enter day: "))
        date_of_birth=(year,month,day)

        if re.match(r"^[a-z\s]{3,30}$",first_name,re.I) and \
            re.match(r"^[a-z\s]{3,30}$",last_name,re.I) and \
            re.match(r"^[a-z][a-z\d._]{2,50}@(gmail|msn|yahoo)$",email,re.I) and \
            re.match(r"^(09[0-9]{9}|0989[0-9]{9})$",mobile,re.I) and \
            re.match(r"^([0-9]{9}|\d{3}-\d{6}-\d)$",national_code,re.I):
            info={ "first name":first_name,
                  "last name":last_name,
                  "email":email,
                  "mobile":mobile,
                  "national code":national_code,
                  "date_of_birth":date_of_birth, }
            info_list.append(info)
            print("person added successfully")

        else:
            print("Invalid input!!!")

    elif option=="2":
        code=input("Enter your code for search: ")
        for person in info_list:
            if person["code"]==code:
                print(person)






