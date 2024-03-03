# Match case is
# switch
numbers = int(input("Enter a number 1-6\n"))# and idea to get the num from 1-6
match numbers: #no break is needed in case of match and case
    case 1:
        print("You have entered 1")
    case 2:
        print("You have entered 2")
    case 3:
        print("You have entered 3")
    case 4:
        print("You have entered 4")
    case 5:
        print("You have entered 5")
    case 6:
        print("You have entered 6")
    case _: # default
        print("No idea")