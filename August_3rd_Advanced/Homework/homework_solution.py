# HOMEWORK by August 4th 
# Try to solve those 2 exercises by the class tomorrow.
# We will go over the solutions at the beginning of the class.

# Exercise #1 - Solution
# Write a function that checks whether inputted string is a palindrome.
# If palindrome return TRUE, else FALSE.
# A string is a palindrome when it reads the same backward as forward.
# Example INPUT: 'abba' OUTPUT: TRUE
# Example INPUT: 'abaa' OUTPUT: FALSE
def is_palindrome_string(x):
    x_reversed = x[::-1] #reversing string x and saving it into a variable
    if x == x_reversed: 
        return True
    else:
        return False

# Testing the solution
string_1 = 'abba'
string_2 = 'hello world'
string_3 = 'abcba'
string_4 = 'acbba'

print('Solution: is string a palindrome')
print('is {} palindrome: {}'.format(string_1, is_palindrome_string(string_1)))
print('is {} palindrome: {}'.format(string_2, is_palindrome_string(string_2)))
print('is {} palindrome: {}'.format(string_3, is_palindrome_string(string_3)))
print('is {} palindrome: {}\n'.format(string_4, is_palindrome_string(string_4)))


# Exercise #2
# Write a function that checks whether inputted integer is a palindrome.
# If palindrome return TRUE, else FALSE.
# A string is a palindrome when it reads the same backward as forward.
# Example INPUT: 121 OUTPUT: TRUE
# Example INPUT: -121 OUTPUT: FALSE
# Example INPUT: 10 OUTPUT: FALSE
def is_palindrome_int(x):
    if x < 0:
        return False
    x = str(x)
    x_reversed = x[::-1]
    if x == x_reversed:
        return True
    return False

# Testing the solution
int_1 = 121
int_2 = -121
int_3 = 23456
int_4 = 12321

print('Solution: is integer a palindrome')
print('is {} palindrome: {}'.format(int_1, is_palindrome_int(int_1)))
print('is {} palindrome: {}'.format(int_2, is_palindrome_int(int_2)))
print('is {} palindrome: {}'.format(int_3, is_palindrome_int(int_3)))
print('is {} palindrome: {}'.format(int_4, is_palindrome_int(int_4)))


