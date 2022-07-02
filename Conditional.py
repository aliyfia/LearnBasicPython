#DataInputA = int(input(" Please input your number A = "))
#DataInputB = int(input(" Please input your number B = "))

#if DataInputA > DataInputB:
#    print("Your number A is bigger then B")
#elif DataInputB > DataInputA:
#    print("Your number B is bigger then A")
#else:
#    print("Your number A and B is equal")



iLight = input("What Color of the Traffic Light ?").lower()

print(iLight)
if iLight == "green":
    cond1 = input("Are you gonna go ?").lower()
    if cond1 == "yes":
        print("Please be careful")
    elif cond1 == "no":
        print("You Get Hit by a Truck")
        print("You Die")
    else:
        print("Are you crazy ?")
elif iLight == "red":
    cond1 = input("Are you gonna go ?").lower()
    if cond1 == "yes":
        cond2 =input("is there are any police ?")
        if cond2 == "yes":
            print("You get a ticket by a police")
        elif cond2 == "no":
            print("You Lucky")
            print("Please Next Time Be Careful")
    elif cond1 == "no":
        print("Stop! until the light turn on to be GREEN")
    else:
        print("Are you crazy ?")
elif iLight == "yellow":
    print("Please be Patience")

