import re

def name_checker(name):
    if type(name) == str and re.match(r"^[a-z\s]{3,30}$",name,re.I):
        print("name is:",name)
        return True
    else:
        print("Error: invalid name!!")
        return False

def family_checker(family):
    if type(family) and re.match(r"^[a-z\s]{3,30}$",family,re.I):
        print("family is:",family)
        return True

    else:
        print("Error: invalid family!!")
        return False

def email_checker(email):
    if type(email) == str and re.match(r"^[a-z][a-z0-9._\s]{3,50}@(gmail|msn|yahoo)[.]com$",email,re.I):
        print("email is:",email)
        return True
    else:
        print("Error: invalid email!!")
        return False

def mobile_checker(mobile):
    if type(mobile) == str and re.match(r"^(09[0-9]{9}|989[0-9]{9})$",mobile):
        print("mobile is:",mobile)
        return True
    else:
        print("Error: invalid mobile number!!")
        return False

def national_code_checker(national_code):
    if type(national_code) == str and re.match(r"^([0-9]{10}|\d{3}_\d{6}_\d)$",national_code):
        print("national code is:",national_code)
        return True
    else:
        print("Error: invalid national code!!")
        return False

def postal_code_checker(postal_code):
    if type(postal_code) == str and re.match(r"^[a-zا-ی0-9.,\s]{3,50}$",postal_code,re.I):
        print("postal code is:",postal_code)
        return True
    else:
        print("Error: invalid postal code!!")
        return False
