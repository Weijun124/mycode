#!/usr/bin/env python3
"""Alta3 Research | RZFeeser
   if, elif, else - A simple program using conditionals to convert numeric score to letter grade."""

def main():
    message= 'You get a grade '

    userinput=input("Please type your score\n")
    # Test user inpuit is digit or not, if it is digit, continue to convert it to int and categories the grade based on the scores
    if userinput.isdigit():
        scores=int(userinput) 
        # Any digit user input should be between 0 and 100, other digit will be invalid for greade
        if scores >100 or scores <0:
            message = "The score is invalid, please contact 911"
        elif scores>=90:
            message = message +"A." 
        elif scores>=80:
            message = message + 'B.'
        elif scores>=70:
            message = message + 'C.'
        elif scores>=60:
            message=message+'D.'
        else:
            message=message+'F. Recycle! Please work hard and See you next year.'
    # Handle the invalid number for user 
    else:
        message="please enter valid number"
    print(message)
if __name__=="__main__":
    main()
