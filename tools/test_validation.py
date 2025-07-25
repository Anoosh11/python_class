from tools.validation import *

# name_checker test
assert name_checker("ALi") == True
assert name_checker("ali1144") == False
print("-"*30)

# family_checker test
assert family_checker("rezaii")== True
assert family_checker("rezaii78") == False
print("-"*30)

# email_ checker test
assert email_checker("Anoosh11@gmail.com") == True
assert email_checker("11gmail") == False


#mobile_checker test
assert mobile_checker("09120456984") and mobile_checker("989900465617") == True
assert mobile_checker("890120456984") == False
print("-"*30)

# national_code_checker test
assert national_code_checker("0023457895") and national_code_checker("002_345789_5") == True
assert national_code_checker("123456") == False
print("-"*30)

#postal_code_checker test
assert  postal_code_checker("تهران abcd.32") == True
assert postal_code_checker("(hj@)") == False