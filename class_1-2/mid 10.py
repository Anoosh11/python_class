n=[]
x=len(n)
while True:
    scores=float(input("Enter score : "))
    if scores <0 or scores >20:
        break
    n.append(scores)
for i in range(x):
  if n[i]<10:
   print(n[i], "fail")
  if 10<=n[i]<=15:
   print(n[i], "success")
   if 15<n[i]<=20 :
    print(n[i], "exellente")
