n=int(input( " enter number: "))
star=0
space=0
for i in range(1,2*n+1):
    space=n
    star=i
    if i <= n:
        print(star * "*")

    if i==n:
        star=n+1
        print(star*"*")

    if i>=n:
        star=2*n-i
        print(star*"*")

