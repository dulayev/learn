while True:

    name=input("input name: ")
    if name == "":
        break

    if name == "Irina":
        age = 41
    elif name == "Alexey":
        age = 42
    else:
        age = -1
        
    if age == -1:
        print("I don't know")
    else:
        print(name  + "'s age is " + str(age))
