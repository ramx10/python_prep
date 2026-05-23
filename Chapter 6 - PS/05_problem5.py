l = ["Gayatri", "Ram", "Sanket", "Aniket"]

name = input("Enter your name: ")

if(name in l):
    print("Your name is in the list:", name)

else:
    print("Your name is not in list:", name)
    l.append(name)
    print("Name added successfully ")
    print("updated list", l)