hh=int(input("give me the start time hour: "))
mm=int(input("give me the start time minute: "))
dd=int(input("give me the duration in the minutes: "))
z=hh*60+mm+dd
hh=z//60
mm=z-hh*60
print("the finish time is=",hh,":",mm)
