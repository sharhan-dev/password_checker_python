password = input("enter here: ")
while len(password) <4 or len(password) >10:
    if len(password) <4:
        print("too short")
    elif len(password) >10:
        print("too long")
    password = input("try again: ")
print('password accepted')