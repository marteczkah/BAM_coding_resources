# Difference in the way objects are passed to the functions

list_1 = [1, 2, 3, 4, 5] #mutable object
string_1 = 'abba' #immutable object

def change_list(original_list):
    list_len = len(original_list)
    if list_len == 0:
        original_list.append(101)
    else:
        original_list[0] = 101

def new_string(old_string):
    old_string = old_string + 'abba'
    return old_string

change_list(list_1)
print(list_1)
new_string(string_1)
print(string_1)
# to actually change the string you would have to
# string_1 = new_string(string_1)
# print(string_1)

# mutable objects are passed by REFERENCE, meaning they will be changed within the funcion
# immutable objectd are passed by VALUE, meaning the actual value of the variable won't be changed