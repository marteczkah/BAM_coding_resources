#File to go over tuples
name = input("What is your name?: ")
age = input("What is your age?: ")
courses = []
n = input("Enter the courses you have taken space each one out with a comma: ")
courses = n.split(",")

print(courses)

person1 = {"name":name, "age": age, "courses": courses}

name = input("What is your name?: ")
age = input("What is your age?: ")
country = input("What country are you from?: ")
course1 = []
n = input("Enter the courses you have taken space each one out with a comma: ")
course1 = n.split(",")

print(courses)
person2 = {"name": name, "age": age, "courses": course1, "country": country}

print("dictionary for person 1: ", str(person1))
print("dictionart for person2: ", str(person2))

print("Same keys in the dictionaries: ", set(person1.keys()).intersection(person2.keys()))
# print(set(person1.keys()).intersection(person2.keys()))


print("Difference in Keys for dictionary: ", set(person2) - set(person1))
# print(set(person2) - set(person1))

person1.update(person2)
print("Update dicitionary person1: ", person1)
