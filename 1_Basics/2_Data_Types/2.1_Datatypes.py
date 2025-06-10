# Data Types in Python

# A. Numeric Types
# 1. int (integer)
x = 16
print(type(x))  # Output: <class 'int'>

# 2. float (Float Point Number)
pi = 3.14
print(type(pi)) # Output: <class 'float'>

# 3. complex (Complex Numbers)
z = 3+4j
print(type(z)) # Output: <class 'complex'>

# B. Text Type
name = 'Aman'
print(type(name)) # Output: <class 'str'>

s1 = "Double quote text sample"
s2 = 'Single quote text sample'
s3 = '''Multi-line text
sample example in Python 
'''

# C. Boolean Type
flag = True
print(type(flag)) # Output: <class 'bool'>

is_valid = False
print(type(is_valid)) # Output: <class 'bool'>

# D. Sequence Types

# 1. List | []
# Ordered, mutable collection of items.
l1 = [1,2,3,4]
print(type(l1)) # Output: <class 'list'>

# Lists can hold multiple data types:
l2 = ['a', True, 3, 4.22]
print(type(l2))

# 2. Tuple | ()
# Ordered, immutable collection of items.
t1 = (1,2,3,4,5,6)
print(type(t1))  # Output: <class 'tuple'>

t2 = ('a', 3, 4.33, False)
print(type(t2))

# 3. range
r = range(11)
print(r) # range(0, 11)
print(list(r)) # Output: [0, 1, 2, 3, 4, ....]


# D. Set Types
# set
# Unordered, mutable collection of unique items.
unique_values = {9,2,3,4,5,5,4,4,2,5,6,7,8}
print(unique_values)
print(type(unique_values)) # Output: <class 'set'>

# E. Mapping Type
# dict | Dictionary
d = {"name":'Aman', "age":'21'}
print(type(d)) # Output: <class 'dict'>
print(d["age"])

# F. None Type
# NoneType
# Represents the absence of a value.s
i = None
print(type(i)) # Output: <class 'NoneType'>