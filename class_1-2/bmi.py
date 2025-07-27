weight=float(input("enter weight (kg) : "))
height=float(input("enter height (cm) : "))
height= height/100

if not weight>0:
    print( " وزن اشتباه است ")
elif not height>0:
    print( " قد اشتباه است ")

bmi=weight/(height**2)
print("bmi is = ",round(bmi,2))

if bmi<18.5:
    print(" کمبود وزن ")
elif 18.5<=bmi<25:
    print(" نرمال ")
elif bmi>=25:
    print( " اضافه وزن ")

