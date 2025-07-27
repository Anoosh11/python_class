length=float(input("Enter length (m) : "))
width=float(input("Enter width (m) : "))

if not length>0 or not width>0:
    print("مقادیر وارد شده صحیح نیست ")

area=length*width

if area<=100:
    print("مجوز صادر میشود")
elif 100<=area<=200:
    print("جریمه پرداخت شود")
else :
    print("!مجوز صادر نمیشود!")
