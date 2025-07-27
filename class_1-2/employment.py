employee=str(input(" جنسیت خود را وارد کنید : "))
age=float(input(" سن خود را وارد کنید : "))

if employee== "مرد" and 20<=age<=30:
    print(" استخدام شود")
elif employee== "زن" and 20<=age<=35:
    print(" استخدام شود ")
else:
    print(" فاقد شرایًط استخدام ")
