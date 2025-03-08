# Modules: A file containing code you want to include in your program.
#          "import" to include a module(built-in or your own module).
#          useful to breakup a large program reusable separate files
#          Random: this module used to make a random choice 
import random

answer=random.randint(1,100)
guesses=[]
guess=0
while True:
    choice=input("Enter your guess(1-100): ")

    if choice.isdigit():
        choice=int(choice)
        guess+=1
        guesses.append(choice)
    
        if choice<answer:
            print("its higher than that")
        elif choice>answer:
            print("its lower than that")
        else:
            print(f"You guess {choice} is correct")
            print ("your guesses:",end=" ")
            for attempts in guesses:
                print(attempts,end=" ")
            print()
            print(f"guesses:{guess}")
            break
    else:
        print("its invalid number")
        print("please enter the number between 1 and 100")
        