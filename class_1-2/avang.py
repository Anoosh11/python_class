n=int(input( "enter number : "))
a=n*" "
star=1
print(a,"O")
for i in range(1,n+1):
   print((n-i)*" "+star*"*",2*i*" "+star*"*")
# O : be onvane markaz dar nazar gerefte shode ast
b=(2*n-6)*"*"
print("(x,z)"+b+"(y,f)")

for i in range(1,n+1):
 if "y":
   print("right")
 if "0":
    print("central")
 if "x":
   print("left")
 if "O":
     print("central")
 if "x":
     print("right")
 if "O":
     print("central")
 if "f":
     print("left")
 print("--------------")