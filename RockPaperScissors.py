import random
bot=[]
chances=3
options=["rock",
            "paper",
            "scissors"]
print("your have 3 health ❤❤❤")
while chances > 0:
    Yourchoice= (input("rock/paper/scissors: "))
    
    bot.append(random.choice(options))
    print(bot)
    
    if bot == "rock" :
            if Yourchoice == "paper":
                print("Congratulations! You won")
                break
            elif Yourchoice =="scissors":
                chances=chances-1
                print("Unfortunately, you lost. Remaining chances:",chances)
            else:
                chances=chances-1
                print("draw")
                

    elif bot == "paper":
            if Yourchoice == "scissors":
                print("Congratulations! You won")
                break

            elif Yourchoice == "rock":
                chances=chances-1
                print("Unfortunately, you lost. Remaining chances:",chances)
            else:
                chances=chances-1
                print("draw")
                

    else:
            if Yourchoice == "paper":
                chances=chances-1
                print("Unfortunately, you lost. Remaining chances:",chances)
            elif Yourchoice=="rock":
                print("Congratulations! You won")
                break
            else:
                chances=chances-1
                print("draw")
print("finish")