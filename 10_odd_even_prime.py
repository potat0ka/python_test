#even no
#odd no
number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Your entered number is even")
elif number % 2 != 0:
    print("Your entered number is odd")


#Any number which have not more than 2 divisible number is called prime number
# A whole number greater than one  which is divisible by  only itself  or one is called prime no

# Algorithm:
# 1. Start
# 2. Input a number (n)
# 3. Initialize `start = 1` and `count = 0`
# 4. Loop from `start = 1` to `n`:
#    - If `n % start == 0`, increment `count` by 1
# 5. After the loop:
#    - If `count > 2`, print "It is a composite number"
#    - Otherwise, print "It is a prime number"
# 6. End

# Pseudocode:
# INPUT number  // Take input from the user
# SET start = 1, count = 0

# LOOP WHILE start <= number
#     IF number % start == 0 THEN
#         count = count + 1
#     ENDIF
#     start = start + 1
# ENDLOOP

# IF count > 2 THEN
#     PRINT "It is a composite number"
# ELSE
#     PRINT "It is a prime number"
# ENDIF



# Input a number
# number = int(input("Enter a number: "))

# # Initialize variables
# start = 1
# count = 0

# # Loop through numbers from 1 to the input number
# while start <= number:
#     if number % start == 0:  # Check if divisible
#         count += 1  # Increment the count
#     start += 1  # Move to the next number

# # Check if the number is prime or composite
# if count > 2:
#     print("It is a composite number")
# else:
#     print("It is a prime number")

#Explanation:

# 1. Divisors:
#    - A prime number has exactly two divisors: 1 and itself.
#    - A composite number has more than two divisors.

# 2. How It Works:
#    - The program checks how many numbers from `1` to `n` divide `n` without a remainder (`n % start == 0`).
#    - If the total divisors (`count`) exceed 2, it's composite; otherwise, it's prime.

# 3. Example Outputs:
#    - Input: `7` → Output: `It is a prime number` (divisors: 1, 7).
#    - Input: `8` → Output: `It is a composite number` (divisors: 1, 2, 4, 8).
#    - Input: `1` → Output: `It is a prime number` (special case).



