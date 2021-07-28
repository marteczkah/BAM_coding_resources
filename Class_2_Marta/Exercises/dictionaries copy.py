
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)

print(student['name'])


#print(student['phone'])
#print(student.get('phone'))
#Make one update to dictionary
student['phone'] = '123-444-6789'


#Make multiple updates at one time
student.update({'name':'Jane', 'age': 26, 'phone': '123-44'})

#Delete a field from dictionary
del student['age']

#Remove item from dictionary and store it into a variable
courses = student.pop('courses')
print(courses)

#Print the length of the dictionary
print(len(student))

#Print the keys of the dictionary
print(student.keys())

#Print the values of the dictionary
print(student.values())

#Print the items of the dictionary
print(student.items())

#How to iterate through a dictionary
for key, value in student.items():
    print(key,value)

