a = int(input("Enter your age: "))

# if statement no 1
if(a%2 == 0):
    print("\nA is even")

else: 
    print ("\nA is odd")

#End of if statement no 1 

# if statement no 2
if(a>18):
    print("\nYou are the above the age of consent")
    print("Good for you")

elif(a<0):
    print("\nYou are trying to be extra smart")

elif(a==0):
    print("\nYou are trying to enter 0 which is not valid age")
else:
    print("\nYour are below the age of the consent")

#End of if statement no 2 
print("\tEnd of program")