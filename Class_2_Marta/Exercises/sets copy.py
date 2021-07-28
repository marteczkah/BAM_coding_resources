cs_courses = {'History', 'Math', 'Physics', 'CompSci'}
#Order will change every time 
print(cs_courses)

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'Math'}
print(cs_courses)

print("=================================")
# Find the values these two sets have in common
art_courses = {'History', 'Math', 'Art', 'Design'}
print("\n Print art course and cs intersection:")
print(cs_courses.intersection(art_courses))

# Find the values these two sets don't have in common
print("\n Print art course and cs difference:")
print(cs_courses.difference(art_courses))


#Union the two list together
print("\n Print cs unionizing with art:")
print(cs_courses.union(art_courses))

