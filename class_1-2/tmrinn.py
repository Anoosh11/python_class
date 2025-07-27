product_list=[]
while True:
    product=input("enter product : ")
    if product.lower()=="exit":
        break
    product_list.append(product)
    lower_list=[]
    for product in product_list:
        lower=product.lower()
        lower_list.append(lower)
    list_gheyre_tekrari=[]
    for product in lower_list:
        if not product in list_gheyre_tekrari:
            list_gheyre_tekrari.append(product)
for product in list_gheyre_tekrari:
     count=lower_list.count(product)
     print("product is :",product, "sell count is :",count*"*")