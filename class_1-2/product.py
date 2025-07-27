products=[]
unique=["mobile","monitor","speaker","mouse"]
while True:
    n=input("enter product:")
    products.append(n)
    if n.lower() == "exit":
        break
for i in range (len(products)):
    if products[i] in unique:
         print("product :",unique[len.unique])
         print("sell count : ",products.count(unique[i])*"*")



