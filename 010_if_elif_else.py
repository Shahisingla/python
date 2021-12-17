y=int(input("enter the year: "))
if y<1582:
    print("Not within Gregorian Calendar")
elif y%4 !=0:
    print("common year")
elif y%100 !=0:
    print("leap year")
elif y%400 !=0:
    print("common year")
else:
    print("leap year")
