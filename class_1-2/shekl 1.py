n=int(input( "enter number: "))

for i in range(1,n+1):
    print(" "*(n-i),i*"*")

print("*"*((n*2)+1))


x=2*n+1
for i in range(x,0,-1):
    print(" "*(n-1),(i-n-1)*"*")

