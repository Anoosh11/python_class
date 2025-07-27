a=int(input("عدد را وارد کنید : "))


for i in range(1,a+1):
    print("*"*i)

for i in range(a):
    for j in range(a):
        if i==0 or i== a-1 or j==0 or j== a-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

for i in range(a,1-1,-1):
    print("*"*i)