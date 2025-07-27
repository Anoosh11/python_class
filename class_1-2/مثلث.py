n=int(input("enter number :"))
star=1
space=n-1
for i in range(1,n+1):
    print(" "*space,star*"*"," "*space)
    space-=1
    star+=2