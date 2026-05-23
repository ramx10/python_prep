a = int(input("Enter your age: "))

# if elif else ladder

if(a>18):
    print("You are the above the age of consent")
    print("Good for you")

elif(a<0):
    print("You are trying to be extra smart")

elif(a==0):
    print("You are trying to enter 0 which is not valid age")
else:
    print("Your are below the age of the consent")


print("End of program")