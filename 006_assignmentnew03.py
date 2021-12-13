hh=int(input("give me the start time hour: "))
mm=int(input("give me the start time minute: "))
dd=int(input("give me the duration in the minutes: "))
z=hh*60+mm+dd
print("the finish time is= ",end="")
print(z//60,z%60,sep=":")
