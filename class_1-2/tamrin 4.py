n=[]
while True:
    name=input("enter your name:")
    n.append(name)
    if name.lower()=="exit":
        n.remove("exit")
        break



for name in n:
    print("i numbers: ",name.count("i".lower()),"j numbers :",name.count("j".lower()))

a=0
for name in n:
    for i in range(len(name)):
        if name[i].lower()=="i":
            a+=1
        if name[i].lower()=="j":
            a+=1
print(a)