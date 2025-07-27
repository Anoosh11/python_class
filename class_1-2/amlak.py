house_list=[]
for i in range(5):
    city=input("enter city name :")
    metrace=int(input("enter metrace number(m): "))
    elevator=input("has an elevator ? YES/NO ")
    parking=input("has a parking lot ? YES/NO ")

    year=int(input("enter year of built :"))
    month=int(input("enter month of built :"))
    day=int(input("enter day of built :"))

    year_of_built=(year,month,day)

    house={"city": city,"metrace":metrace," elevator":elevator,"parking lot":parking,"year_of_built":year_of_built}
    house_list.append(house)
    print("-"*30)
for i in range(len(house_list)):
    print(house_list[i])

