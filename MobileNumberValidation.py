# This code checks whether it's a valid mobile or not

# validations
# 1. Should contain 10 digits
# 2. Should start not start with 0
mobileNumber = input("Please enter the mobile number")
if len(mobileNumber) != 10:
    print("Mobile  doesn't have 10 numbers --> Invalid")
elif not mobileNumber.isdigit():
    print("Mobile doesn't contain all digits --> Invalid")
elif mobileNumber.startswith(0):
    print("Mobile shouldn't start with zero --> Invalid ")
else:
    print("Seems a valid mobile")
