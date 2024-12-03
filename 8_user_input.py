# input("string") -> str

age = input("Enter your age?")
if isinstance(age,str) and not age.isdigit():
    print("invalid age")
else:
    age = int(age)  # Convert the valid input to an integer

    if age <= 0 or age >= 115:  # Check for invalid age range
        print("Your Entered Age Is WRONG")
    elif age > 0 and age < 13:  # Age between 1 and 12
        print("You are a child")
    elif age >= 13 and age <= 20:  # Age between 13 and 20
        print("You are a teenager")
    elif age > 20 and age <= 60:  # Age between 21 and 60
        print("You are an adult")
    else:  # Remaining valid ages (61 to 114)
        print("You are old")