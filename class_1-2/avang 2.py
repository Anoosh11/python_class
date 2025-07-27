n=int(input("enter number : "))

print((n+2)*" ","O")
for i in range(n):
    print(i*" ")

print("C",n*" ","B",n*" ","A")

makan="A","B","C"
jahat="right","left","center"

for i in range(2,n+1):
    if "A" :
     makan=="A"
     jahat=="right"
     print("right")
     if "B":
        makan=="B"
        jahat==("right")
        print("center")
     if "C":
         makan=="C"
         jahat=="left"
         print("left")
         makan=="B"
         jahat=="right"
         print("center")
         print("------")
     if "B":
         makan=="B"
         jahat=="left"
         print("center")