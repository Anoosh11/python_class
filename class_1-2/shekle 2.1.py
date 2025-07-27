n=int(input("enter number: "))
star=0
space=0
for i in range(1,2*n+1):
    if i<=n:
        space=n
        star=i
        print(" "*space,star*"*")
    if i ==n :
        print("*"*(2*n+2))
    if i>=n:
        star=2*n-i
        space=i-n
        print(" "*space,star*"*")