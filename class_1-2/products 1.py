products=["mobile","mobile","speaker","monitor","speaker","monitor","mobile","mouse"]
l=[]
for i in range (len(products)):
    if products[i] not in l:
        l.append(products[i])
        print("product :",products[i])
        print("sell count:",products.count(products[i])*"*")