username = input("\tEnter username : ")

if(len(username)<10):
    print("Your username contains less than 10 character", username)
    print("\tLength of character is",len(username))

else:
    print("Your username contains more than 10 character", username)
    print("\tLength of character is",len(username))