import readline
from numpy import random
question1 = input("Do you wish to generate random numbers (1) or input your own (2)? >")
print()

if question1 == "1":
    range1 = input("Enter start of the range or leave the default one (1) >")
    if range1 == "":
        range1 = 1
    else:
        range1 = int(range1)
    range2 = input("Enter end of the range or leave the default one (1000000000) >")
    if range2 == "":
        range2 = 1000000000
    else:
        range2 = int(range2)
    print()

    question2 = input("How many runs do you wish to perform? >")
    runs1 = int(question2)
    print()

    f = open("output.txt", "a")
    while runs1 != 0:
        number1 = random.randint(range1, range2)
        number2 = number1
        basenumber = number1
        count = 0

        while number1 != 1:
            if number1%2 == 0:
                print(number1, "is even (/2)")
                number1 = number1/2
                print(number1, "=", number2, "/ 2")
            else:
                print(number1, "is odd (3x+1)")
                number1 = 3*number1+1
                print(number1, "=", "3 *", number2, "+ 1")
            number2 = number1
            count = count+1
            print()
        
        write1 = 'Number '+ str(basenumber) + ' taken ' + str(count) + ' operations to get to 1.'
        write2 = str(basenumber)+";"+str(count)
        print(write1)
        print()
        f.write('\n')
        f.write(write2)
        runs1 = runs1-1
    f.close()

elif question1 == "2":
    continue1 = "y"
    while continue1 == "y":
        number1 = float(input("Please insert number > "))
        print()
        number2 = number1
        basenumber = number1
        count = 0

        while number1 != 1:
            if number1%2 == 0:
                print(number1, "is even (/2)")
                number1 = number1/2
                print(number1, "=", number2, "/ 2")
            else:
                print(number1, "is odd (3x+1)")
                number1 = 3*number1+1
                print(number1, "=", "3 *", number2, "+ 1")
            number2 = number1
            count = count+1
            print()
        
        write1 = 'Number '+ str(basenumber) + ' taken ' + str(count) + ' operations to get to 1. (Sheet version: ' + str(basenumber)+";"+str(count) + ')'
        print(write1)
        print()

        continue1 = input("Do you wish to enter another number? y/n >")
        print()
    print("Ending...")

else:
    print("Please enter only one of the valid options. Ending program...")