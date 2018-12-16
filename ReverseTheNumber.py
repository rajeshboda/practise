# this snippet reverse the given number and prints it.
numberToReverse = int(input("Please enter the number to reverse -->  "))
while numberToReverse > 0:
    print(numberToReverse % 10, end='')
    numberToReverse //= 10
