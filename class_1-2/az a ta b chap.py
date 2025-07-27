a=int(input("عدد اول را وارد کنید : "))
b=int(input("عدد دوم را وارد کنید : "))
for i in range(a,b+1):
    print(i)
if a>b:
    for i in range(a,b-1,-1):
        print(i)