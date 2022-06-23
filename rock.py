while True:
    a=input("do you want to play yes/no")
    if a=="yes":
        # computer=["1:stone","2:paper","3.sscissors"]
        b=input("enter-:stone/paper")
        if b=="stone":
            print("computer-:sscissor")
            print("you are right")
            c=input("enter-:sscissors/paper")
            if c=="paper":
                print("computer-:stone")
                print("you are right")
                d=input("enter-:stone/ssicssors")
                print("computer-:paper")
                if d=="stone":
                    print("you are right")
                else:
                    if d=="ssicssors":
                        print("you are worng")
            else:
                if c=="ssicssor":
                    print("you are worng")
        else:
            if b=="paper":
                print("you are wrong")
    else:
        print("thank you")
        break