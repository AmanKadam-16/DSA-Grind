# OUTPUT in Python
# print()
print('Hello, World!')

# print on next line | use backward slash n ie. `\n`
print('This is line one \nThis is line two \nThis is line three')

# INPUT in Python
# Taking Input
name = input('Enter your name : ')
print(f'Greetings {name}.')

# Converting Input to Integer
value1 = int(input('Enter value one : '))
value2 = int(input('Enter value two : '))
print(f'Sum of {value1} and {value2} is {value1+value2}.')

# Multiple Inputs in One Line
v1, v2 = input('Enter 2 values to be multiplied with space separated. ').split()
print(f'The multiplication of {v1} and {v2} is {int(v1)*int(v2)}.')

# If needed, convert them to integers:
v3, v4 = map(int, input('Enter both values to be added with space separated : ').split())
print(f'The addition of {v3} and {v4} is {v3+v4}.')