a=int(input("Enter a : "))
for i in range(-a,a+1):
    print(i)
if a<0:
    for i in range(a,-a+1):
        print(i)