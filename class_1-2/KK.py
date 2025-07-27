product_list=["Mobile","Mobile","speaker","monitor","speaker",'monitor',"mobile","mouse"]
lower_list=[]
for product in product_list :
    product.lower()
    lower_list.append(product.lower())
print(lower_list)
gheyre_tekrari_list=[]
for product in lower_list :
    if not product in gheyre_tekrari_list:
        gheyre_tekrari_list.append(product)
print(gheyre_tekrari_list)
for product in gheyre_tekrari_list :
    count=lower_list.count(product)
    print(product,count*"*")
