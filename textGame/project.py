answer = input("do you want to play this game? [yes/no]: ")

if answer == "yes" :
    print("welcome to game")
    answer = input("do you want to go jungle or cave? [jungle/cave]: ")
    if answer == "jungle" :
        print("you see the hungry tiger. tiger will eat you ")
    elif answer == "cave" :
        print("you seen the beer in font cave")
        answer = input("do you want to fight or run? [fight/run]: ")
        if answer== "fight" :
            print("bear is too much strong. you lose the game!")
        else:
            print("wow! still alive")

else:
    print("the game closed")