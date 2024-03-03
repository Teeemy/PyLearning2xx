#Write a program that calculates and displays the letter grade for a
# given numerical score (e.g A,B,C,Dor F)based on the ff grading scale
#input score -89
#output-B
#A  90-100
#B  80-89
#C 70-79
#D 60=69
#F 0-59
#if,elif,else

#every problem statement must be div into 3 steps
# step 1 : figure out the inputs
#step 2: logic i.e print A if scale is <= 100 and scale >= 90
# step 3: print output

scale = int(input("Enter your grade: \n"))

if scale >= 90 and scale <= 100:
    print("Grade A")
elif scale >= 80 and scale <= 89:
        print("Grade B")
elif scale >= 70 and scale <= 79:
        print("Grade C")
elif scale >= 60 and scale <= 69:
        print("Grade D")
elif scale >= 0 and scale <= 59:
        print("Grade F")
else:
    print("Invalid Input")