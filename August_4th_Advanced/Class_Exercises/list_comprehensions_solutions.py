# List Comprehensions Exercises

# Exercise 1
# Create a list of integers from 1 to 100 using list comprehensions.
list_1 = [x for x in range(1,101)]
print('list 1:\n', list_1, '\n')

# Exercise 2
# Create a list of all the characters in string 'hello world', not including the whitespace ' '.
string_1 = 'Hello World'
list_2 = [x for x in string_1 if x != ' ']
print('list 2:\n', list_2, '\n')

# Exercise 3
# Create a list of squares of integers in the range from -10 to 0.
list_3 = [x**2 for x in range(-10,1)]
print('list 3\n', list_3, '\n')

# Exercise 4
# Create a list of even integers from 1 to 100.
list_4 = [x for x in range(1,101) if x % 2 == 0]
print('list_4\n', list_4, '\n')

# Exercise 5
# Create a list of odd integers from 1 to 100. 
list_5 = [x for x in range(1,101) if x %2 != 0]
print('list 5\n', list_5)