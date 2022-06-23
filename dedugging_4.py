from lib2to3.pgen2.token import LESS
import random
live = True
stamina = 10
def report():
    if stamina > 8:
        print ("The alien is strong! It resists your pathetic attack!")
    if stamina > 5:
        print ("With a loud grunt, the alien stands firm.")
    if stamina>3:
        print ("Your attack seems to be having an effect! The alien stumbles!")
    if stamina > 0:
        print ("The alien is certain to fall soon! It staggers and reels!")
    else:
        print ("That's it! The alien is finished!")
report()
def fight():
        response = input("Enter a move 1.Hit 2.attack 3.fight 4.run")
        response=random.randint(0, stamina)
        less=respon
        if "hit" in response or "attack" in response:
            respon=random.randint(0, stamina)
            stamina=respon
        elif "fight" in response:
            print ("Fight how? You have no weapons, silly space traveler!")
        elif "run" in response:
            print ("Sadly, there is nowhere to run.")
            print ("The spaceship is not very big.")
        else:
            print ("The alien zaps you with its powerful ray gun!")
            return True
        return False
if live==True:
    print ("\nThe alien lives on, and you, sadly, do not.\n")
else:
    print ("\nThe alien has been vanquished. Good work!\n")
fight()