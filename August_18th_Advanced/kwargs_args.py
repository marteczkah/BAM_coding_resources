def multiply(my_list):
    mult = 1
    for integer in my_list:
        mult *= integer
    return mult

def multiply_args(*args):
    mult = 1
    for integer in args:
        mult *= integer
    return mult

def two_or_more(num1, num2, *nums):
    result = num1 + num2
    if len(nums) > 0:
        for num in nums:
            result += num
    return result

# my_list = [1, 2, 3, 4, 5]
# result = multiply(my_list)
# print(result)

# res = multiply_args()
# print(res)

# var = two_or_more(101, 101, 101)
# print(var)

def one_or_more(title, **info):
    print(title)
    for key, value in info.items():
        print('Key {}, Value: {}'.format(key, value))

one_or_more('Hello World', x = 8, y = 9, z = 'hello')

