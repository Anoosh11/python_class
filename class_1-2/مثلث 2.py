n=int(input("enter number :"))
star=(n*2)-1 #az adade fard shoro kardam
space=0
for i in range(1,n+1):
    print(" "*space,"*"*star," "*space)
    star-=2
    space+=1
