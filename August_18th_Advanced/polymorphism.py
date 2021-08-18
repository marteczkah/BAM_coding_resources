# parent class
class Dog:
    sound = 'woof woof'
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print('{} is {} years old.'.format(self.name, self.age))

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def description(self):
        print('This is a cat')


dog_1 = Dog('Snack', 10)
cat_1 = Cat('Maya', 3)

dog_1.description()
cat_1.description()


