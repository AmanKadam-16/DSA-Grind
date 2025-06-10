# if else statements in Python

# Example 1 | Even / Odd
num = 33
if num % 2 == 0:
    print(f'{num} is a Even number.')
else:
    print(f'{num} is an Odd number.')


# Example 2 | Problem Statement
# 🎯 Requirements:
# If the age is less than 5, the entry is free.

# If the age is between 5 and 12 (inclusive), the ticket price is ₹100.

# If the age is between 13 and 59 (inclusive), the ticket price is ₹200.

# If the age is 60 or above, the ticket price is ₹120.
age = 4
# Solution :
if age < 5:
    print('Entry is free.')
elif age in range(5,13):
    print('The ticket price is ₹100')
elif age in range(13,60):
    print('The ticket price is ₹200')
elif age >= 60:
    print('The ticket price is ₹120')
else :
    print('No Result.')