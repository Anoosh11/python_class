n=int(input( "enter number :"))

for i in range(1,2*n+1):
    star=0
    space=0
    if i<=n:
        star=i
        space=n-i
        print(" "*space,star*"*")
    if i ==n :
        print((n+1)*"*")
    if i>=n:
        star=2*n-i
        space=i-n
        print(" "*space,star*"*")

