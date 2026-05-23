marks1 = int(input("Enter Marks 1: "))
marks2 = int(input("Enter Marks 2: "))
marks3 = int(input("Enter Marks 3: "))

# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage >= 40 and marks1 >=33 and marks2 >=33 and marks3 >=33):
    print("You are Pass") 
    print("Congrats you got", total_percentage, "%")

else:
    print("You Failed") 
    print("You got", total_percentage, "%")
    print("Try again next year")
