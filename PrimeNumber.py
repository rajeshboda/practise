# this snippet finds whether the number is prime or not.
num = int(input("Please enter the number to check -->  "))
for i in range(2, num // 2 + 1):
    if num % i == 0:
        print("Not a prime number!")
        break
else:
    print("Prime Number!")
