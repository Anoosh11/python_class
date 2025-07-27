n=int(input( "enter number : "))
space=0
star=1
for i in range(1,2*n):
    if i<=n:
        space=n-i
        print(" "*space,star*"*"," "*space)
        star+=2
    if i>n:
        space=i-n
        star=(2*n-i)*2-1
        print(" "*space,star*"*"," "*space)

