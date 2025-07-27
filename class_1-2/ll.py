mostatil=0
motevaziol_azla=0
lozi=0

mostatil+=1
prime_list=[]

mostatil+=1
for i in range(2,1001):
    lozi+=1
    mostatil+=2
    count = 0
    mostatil+=1
    for j in range(2,i):
        lozi+=2
        mostatil+=1
        if i%j==0:
            mostatil+=1
            count+=1
    if count == 0:
        lozi+=1
        mostatil+=1
        prime_list.append(i)

motevaziol_azla+=3
print(prime_list)
print("sum is : ", sum(prime_list))
print("count is : ",len(prime_list))
print("mostatil is : ", mostatil)
print("lozi is : ", lozi)
print("motevaziol_azla is : ", motevaziol_azla)

