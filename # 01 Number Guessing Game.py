# 01. Number Guessing Game

import random

def guessing(num):
    while num != num_select:
        if num < num_select:
            print('It is too low!', '\n')
            num = int(input("Enter your number: ")) #overwrite the num
        elif num > num_select:
            print('It is too high!', '\n')
            num = int(input("Enter your number: ")) #overwrite the num
        else:
            break
    print('Perfect match!') #num == num_select

num_select = random.randrange(0,21)
#randrange() returns a randomly number from a specified range (start, end, step)

given = int(input("Enter your number: ")) #enter an integer for comparison
print('random number:', num_select) #can omit, just for verification
guessing(given) #call function
 