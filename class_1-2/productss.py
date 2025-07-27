products=[]
while True:
    n=input("enter products : ")
    products.append(n.lower())
    if n.lower() == "exit":
        break
l=[]
for i in range (len(products)-1):
    if products[i] not in l:
        l.append(products[i])
        print("product :",products[i])
        print("sell count:",products.count(products[i])*"*")