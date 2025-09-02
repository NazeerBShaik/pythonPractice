#The match statement is used to perform different actions based in different conditions
#instead of writing many if...else statements, you can use the match statement
#The match statement selects one of many code blocks to be executed.
day = 4
match day:
    case 1: print("Monday") #SHORT HAND NOTES WRITED
    case 2: print("Tuesday")
    case 3: print("Wednesday")
    case 4: print("Thursday")
    case 5: print("Friday")
    case 6: print("Saturday")
    case 7: print("Sunday")
    case _: print("Looking forward to the Weekend")#Default Value "_" character as the last case value if you want a code block to execute when there are not other matches
#COMBINE VALUES
#use the pipe character | as an operator in the case evaluation to check for more than one value match in one case
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5:
        print("Today is a weekday")
    case 6 | 7:
        print("I love weekends! ")
#if statement as guards
month = 5
day = 4
match day:
    case 1 | 2 | 3 | 4 | 5 if month == 4:
        print("Today is a weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("Today is a weekday in May")
    case _:
        print("No match")        
        