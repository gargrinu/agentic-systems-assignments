# Number Operations with Error Handling

try:
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

except ValueError:
    print("Invalid input")
    
else:
    if b == 0:
        print("Cannot divide by zero")
    else:
        print("Sum:", a + b)
        print("Division:", a / b)


# User Information and String Concatenation

try:
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    age1 = int(input("Enter age: "))

except ValueError:
    print("Invalid age input")

else:
    if age1 < 0:
        print("Age cannot be negative")
    else:
        full_name = first_name + " " + last_name
        print("Full Name:", full_name)
        print("You will be", age1 + 1, "next year")


# Age Category and Eligibility Checker

try:
    name = input("Enter your name: ")
    age2 = int(input("Enter your age: "))

except ValueError:
    print("Invalid age input")

else:
    if age2 < 0:
        print("Age cannot be negative")
    else:
        print("Hello", name)
        if age2 < 13:
            print("You are a Child")
            print("You are not eligible to vote")
        elif age2 >= 13 and age2 <= 17:
            print("You are a Teenager")
            print("You are not eligible to vote")
        elif age2 > 17 and age2 <= 59:
            print("You are an Adult")
            print("You are eligible to vote")
        else:
            print("You are a Senior Citizen")
            print("You are eligible to vote")
