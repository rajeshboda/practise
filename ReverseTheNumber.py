# this snippet reverse the given number and prints it.
numberToReverse = int(input("Please enter the number to reverse -->  should be a number"))
while numberToReverse > 0:
    print(numberToReverse % 10, end='')
    numberToReverse //= 10
