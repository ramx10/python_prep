p1 = "Make a lot of money"
p2 = "Buy now"
p3 = "Subcribe now"
p4 = "click this"

message = input("Enter your message : ")

if((p1 in message ) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("This message is spam ")

else:
    print("This comment is not spam ")
