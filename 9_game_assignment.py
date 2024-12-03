# 90

# guess number ? 40
# hint low
# guess number ? 100
# hint hing
# ..
# .
# ..
# .

# user input marks percentage
# WAP to find first,second,third division or fail

# Input: Total marks scored by the student
marks = input("Enter your marks: ")

# Validate if the input is numeric
if not marks.isdigit():
    print("Invalid input! Please enter a number.")
else:
    marks = int(marks)  # Convert the valid input to an integer
    # Determine the division based on marks
    if marks < 0 or marks > 100:  # Marks must be in the range of 0-100
        print("Invalid marks! Please enter a value between 0 and 100.")
    elif marks >= 60:  # 60 or more is First Division
        print("You got First Division!")
    elif marks >= 50:  # 50 to 59 is Second Division
        print("You got Second Division!")
    elif marks >= 40:  # 40 to 49 is Third Division
        print("You got Third Division!")
    else:  # Less than 40 is a Fail
        print("You failed the exam.")

# Explanation:
# 1. Input Validation:
#    - The program first checks if the input is numeric using `isdigit()`.
#    - If the input is invalid (e.g., `"abc"`, `"-10"`), it prints an error message.

# 2. Valid Marks Range:
#    - Marks must be between 0 and 100.
#    - If `marks < 0` or `marks > 100`, it prompts the user to enter a valid range.

# 3. Divisions Based on Marks:
#    - First Division: Marks >= 60.
#    - Second Division: Marks between 50 and 59.
#    - Third Division: Marks between 40 and 49.
#    - Fail: Marks < 40.

# 4. Output Messages:
#    - The program outputs the respective division or failure based on the marks entered.

# - `75` →  `You got First Division!`
# - `55` →  `You got Second Division!`
# - `45` →  `You got Third Division!`
# - `30` →  `You failed the exam.`
# - `-5` →  `Invalid marks! Please enter a value between 0 and 100.`
# - `"abc"` →  `Invalid input! Please enter a number.`