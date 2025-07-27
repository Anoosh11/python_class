a=int(input("سطر و ستون ر ا وارد کنید : "))

for i in range(a):
    for j in range(a):
        if i == 0 or i == a - 1 or j == 0 or j == a - 1:
            print("*", end="")
        else:
            print(" ", end="")
        print()