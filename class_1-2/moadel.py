score_1=float(input("enter score 1 : "))
score_2=float(input("enter score 2 : "))
score_3=float(input("enter score 3 : "))

if not 0<=score_1<=20:
    print("score 1 is invalid !!!")
if not 0<=score_2<=20:
    print("score 2 is invalid !!!")
if not 0<=score_3<=20:
    print("score 3 is invalid !!!")


average=(score_1+score_2+score_3)/3
print("average is:",round(average,2))

shahrieh=1000
ezafeh_shahrieh=1000
if average<10:
    ezafeh_shahrieh*=3
    jarimeh = ezafeh_shahrieh - shahrieh
    total=shahrieh+ezafeh_shahrieh
    print("( مردود شدید )","   ",": شهریه ",shahrieh," : جریمه ",ezafeh_shahrieh,": کل ",total)

if 10<=average<12:
    ezafeh_shahrieh+=500
    jarimeh = ezafeh_shahrieh - shahrieh
    total=shahrieh+ezafeh_shahrieh
    print("(قبول)","   ","  شهریه : ",shahrieh,"  جریمه : ",ezafeh_shahrieh,"  کل : ",total)

elif 12<=average<16:
    jarimeh = ezafeh_shahrieh - shahrieh
    total=shahrieh+ezafeh_shahrieh
    print( "(قبول خوب) ","   "," شهریه : ",shahrieh,"  جریمه : ",ezafeh_shahrieh,"  کل : ",total)

elif 16<=average<18:
   takhfif=(shahrieh*30)/100
   total=shahrieh-takhfif
   print("(قبول عالی)","   ","  شهریه : ",shahrieh,"  تخفیف : ",takhfif,"  کل : ",total)

elif 18<=average<20:
    takhfif=(shahrieh*70)/100
    total=shahrieh-takhfif
    print("(قبول ممتاز) ","   ","  شهریه : ",shahrieh,"  تخفیف :  ",takhfif,"  کل : ",total)
