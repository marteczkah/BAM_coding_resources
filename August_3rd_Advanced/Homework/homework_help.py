# Help for the homework
# Since we haven't covered functions yet and you
# will need them for homework, here is a quick overview of 
# how functions work. We will cover functions more later in the class.

# this function prints "Hello World", it does not accept any parameters
def hello_world():
    print("Hello World") #this is the body of the function
    # indentation in Python is important, the whole body of the function
    # has to be indented

print("function hello_world")
hello_world() #calling on the function hello_world()
# as you can see by running this function, you will see "Hello World"
# printed in the terminal

# this function is accepting one parameter
def print_number(number_1):
    print("passed number:", number_1)

# now we can try calling on the function print_number
print("\nfunction print_number")
print_number(5)

# now something more similiar to homework, we are going to use return keyword
def return_string(number_1):
    return ("passed number: {}").format(number_1)

# calling on the function, we are going to save the returned value into a variable
# and then print it
print("\nfunction return_string")
returned_string = return_string(7)
print(returned_string)

#lastly, a more complicated function
#it is similar to one of the homework exercises
#but it swaps the last elements of 2 strings, instead of the 1st ones
#and returns them as a list
def swap_last(string_1, string_2):
    new_1 = string_1[:-1] + string_2[-1]
    new_2 = string_2[:-1] + string_1[-1]
    return [new_1, new_2]

#now let's try the swap_last function
print("\nfunction swap_last")
str_1 = "hello" #first string to pass as a parameter
str_2 = "world" #second string to pass as a parameter
swapped = swap_last(str_1, str_2)
print(swapped)

# we are going to cover functions more in depth later in the course
# this is just to help you with the homework :) 
