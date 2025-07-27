score_1=float(input("Enter score 1 : "))
score_2=float(input("Enter score 2 : "))
score_3=float(input("Enter score 3 : "))

if not 0<=score_1<=20:
    print( " نمره مجاز نیست ")
elif not 0<=score_2<=20:
    print( "نمره مجاز نیست ")
elif not 0<=score_3<=20:
    print( "نمره مجاز نیست ")


average=(score_1+score_2+score_3)/3
print("average score is :",round(average,2))

if 0<=average<10:
     print("fail")
if 10<=average<12:
     print("pass - exam")
if 12<=average<17:
     print("pass")
if 17<=average<=20:
     print("pass - exellent")
else:
    print("invalid !!!")

if score_1 > score_2 and score_1 > score_3:
     print( "score 1 is the greatest score" )
elif score_2 > score_3:
    print( "score 2 is the greatest score" )
else:
    print( "score 3 is the greatest score" )
