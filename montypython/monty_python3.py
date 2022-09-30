#!/usr/bin/python3
"""Alta3 Research | RZFeeser
  Conditionals - Life of Brian guessing game without a while True loop."""

round = 0
answer = " "

while round < 3 and (answer != "Brian" and answer !="Shrubbery"):
    round += 1  
    answer = input('Finish the movie title, "Monty Python\'s The Life of ______": ')
    answer=answer.title()
    if answer == "Brian":
        print("Correct!")
    elif answer == "Shurbbery":
        print("You gave the super secret answer!")
    elif round == 3:
        print("Sorry, the answer was Brian.")
    else: 
        print("Sorry. Try again!")

