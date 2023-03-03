import  readline

number1 = float(input("Please insert number > "))
print()
basenumber = number1
count = 0

f = open("final.txt", "a")
f.write('\n')
while number1 != 1:
    if number1%2 == 0:
        print(number1, "is even (/2)")
        number1 = number1/2
        print(number1, "=", basenumber, "/ 2")
        write1 = str(number1) + " = " + str(basenumber) + " / 2"
        f.write(write1)
        f.write('\n')
    else:
        print(number1, "is odd (3x+1)")
        number1 = 3*number1+1
        print(number1, "=", "3 *", basenumber, "+ 1")
        write1 = str(number1) + " = " + "3 * " + str(basenumber) + " + 1"
        f.write(write1)
        f.write('\n')
    basenumber = number1
    count = count+1
    print()
print("Final count of runs is", count)

write1 = 'Final count of runs is ' + str(count)
f = open("final.txt", "a")
f.write('\n')
f.write(write1)
f.close()