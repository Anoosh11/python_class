n=int(input("enter number :"))

for i in range(1,n+1):
    print(i*"*"," "*(n-i))

print((n+1)*"*")

for i in range(n,1-1,-1):
    print(i*"*"," "*(n-i))