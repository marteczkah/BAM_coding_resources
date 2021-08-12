# Exercise 1 - Solution
# Write a function that checks if ANY number in a list is even. Return true if yes, else return FALSE.
def is_even(list_1):
    for x in list_1:
        if x % 2 ==0:
            return True
    return False

# Checking solution
list_1_1 = [2, 4, 5, 6, 11]
list_1_2 = [3, 5, 7, 9]
print('Exercise 1')
print('Checking if [2, 4, 5, 6, 11] has an even number:', is_even(list_1_1))
print('Checking if [3, 5, 7, 9] has an even number:', is_even(list_1_2), '\n')

# Exercise 2 - Solution
# Write a function that returns a list of even numbers in a list. 
# Example INPUT: [2, 4,5, 7, 8, 9, 10] OUTPUT: [2,3,8,10]
def list_even(list_1):
    to_return = []
    for x in list_1:
        if x % 2 == 0:
            to_return.append(x)
    return to_return

# Checking solution
list_2_1 = [2, 4,5, 7, 8, 9, 10]
print('Exercise 2')
list_2_1_even = list_even(list_2_1)
print('Even number from list [2, 4,5, 7, 8, 9, 10]: ', list_2_1_even, '\n')

# Exercise 3 - Solution
# Write a function that reads a list and returns a list without repetition in values.
# Example INPUT: [2, 2, 3, 4, 5, 3, 7, 8, 8] OUTPUT: [2,3,4,5,7,8]
def list_no_repetition(list_1):
    set_1 = set(list_1)
    return list(set_1)

# Checking solution
list_3_1 = [2, 2, 3, 4, 5, 3, 7, 8, 8] 
list_3_1_no_rep = list_no_repetition(list_3_1)
print('Exercise 3')
print('List [2, 2, 3, 4, 5, 3, 7, 8, 8] with no repetition:', list_3_1_no_rep, '\n')

# Exercise 4 - Solution
# Write a function that reads an integer and returns a reverse of the integer.
# Example INPUT: 123 OUTPUT: 321
# Example INPUT: -123 OUTPUT: -321
def reverse_integer(num):
    if num == 0:
        return num
    negative = None
    if num < 0:
        negative = True
    else:
        negative: False
    num = abs(num)
    reversed = 0
    while num != 0:
        last_digit = num % 10
        reversed = reversed * 10 + last_digit
        num = num//10
    if negative:
        return -reversed
    else:
        return reversed

# Checking solution
int_1 = 123
int_2 = -123
int_1_rev = reverse_integer(int_1)
int_2_rev = reverse_integer(int_2)
print('Exercise 4')
print('Reverse of integer {} is {}'.format(int_1, int_1_rev))
print('Reverse of integer {} is {}\n'.format(int_2, int_2_rev))


# Exercise 5 - Solution
# Given two lists sorted in increasing order, create and return a merged
# list of all the elements in sorted order. You may modify the passed in lists.
# Ideally, the solution should work in "linear" time, making a single
# pass of both lists. (meaning you can't use nested for loops)
def linear_merge(list1, list2):
  result = []
  while len(list1) and len(list2):
    if list1[0] < list2[0]:
      result.append(list1.pop(0))
    else:
      result.append(list2.pop(0))

  result.extend(list1)
  result.extend(list2)
  return result

# Checking solution
list_5_1 = [1, 3, 4, 5, 6, 7, 9, 10, 11]
list_5_2 = [2, 4, 5, 6, 101, 121, 200]
lists_combined = linear_merge(list_5_1, list_5_2)
print('Exercise 5')
print('Combined [1, 3, 4, 5, 6, 7, 9, 10, 11] and [2, 4, 5, 6, 101, 121, 200] is {}'.format(lists_combined))