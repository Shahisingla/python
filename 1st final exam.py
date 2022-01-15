secret_number=777
n=int(input("Enter the number: "))
while n!=secret_number:
    if n<secret_number:
        print("ha ha ! you are stuck in my loop! your guessed number is smaller than the secret number")
    elif n>secret_number:
           print("ha ha ! you are stuck in my loop! your guessed number is larger than the secret number")
    n=int(input("try again"))
print("well done, muggle! you are free now")
