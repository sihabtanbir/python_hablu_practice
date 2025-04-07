import random

RandomNumber = random.randrange(1,101)

userInput = int(input("Guess the number (1-100): "))

if userInput > RandomNumber :
    print(f"random number is {RandomNumber}")
    print("the number to high")
elif RandomNumber>userInput :
    print(f"random number is {RandomNumber}")
    print("the number to low")

else:
    print("yes, you matched the number")
