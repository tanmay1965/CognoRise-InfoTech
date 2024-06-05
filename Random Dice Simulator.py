n=int(input('Enter number of sides for the dice:-)'))

op='y'
import random
while op=='y':
    die_roll=random.randint(1,n)
    print("DICE:",die_roll)
    op=input("if u want to continue press y: ")
