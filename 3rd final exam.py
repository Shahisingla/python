input_number=int(input("please enter a number: "))
a=0
b=1
if (input_number%1==0 and input_number>0):
    while (input_number//b>0):
        b=b*10
        a=a+1
    print(a)
else:print("input is not valid")


