# Operators Exercises

# Exercise #1 - Solution
# Create a list of integers from 1 to 100 and print it.
list_1 = []
for x in range(1,101):
    list_1.append(x)
print(list_1)

# Exercise #2 - Solution
# Having two lists below, create another list with elements present in list_1
# but not in list_2.
list_1 = [1, 6, 7, 101, 23, 45, 66, 78, 89, 0, -101, -90]
list_2 = [1, 6, -101, 66, -5, 10, 23, 89, -90, 88, 58, 76]

list_3 = []
for x in list_1:
    if x not in list_2:
        list_3.append(x)
print(list_3)

# Exercise #3 - Solution
# Create a list of 10 random integers in range 0 to 100.
# Each itration of the program should generate a different list.
from random import randint
list_4 = []
for x in range(0,10):
    list_4.append(randint(0,100))
print(list_4)