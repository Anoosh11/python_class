n=int(input( " adad  mosalase aval ra vared konid : "))

for i in range(1,n+1):
    print(" "*n,i*"*")
    if i==n:
        print("*"*(2*n+2))

for i in range(n,0,-1):
    print(" "*(n-i),"*"*i)

