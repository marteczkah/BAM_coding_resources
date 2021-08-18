# parent class
class Dog:
    sound = 'woof woof'
    def __init__(self, __name, age):
        self.__name = __name
        self.age = age
    
    def description(self):
        print('{} is {} years old.'.format(self.__name, self.age))
    
    def get_name(self):
        return self.__name

    def get_size(self): # abstract method
        raise NotImplementedError('Subclass must implement abstract method')

# child class
class Pomeranian(Dog):
    size = 'small'
    breed = 'pomeranian'

    def __init__(self, __name, age, color='multi'):
        super().__init__(__name, age)
        self.color = color
    
    def description(self):
        print('this a child class')
    
    def get_size(self):
        print('Pomeranians are {} dogs.'.format(self.size))

snack = Dog('Snack', 10)
snack.get_name()
jack = Pomeranian('Jack', 3, 'pink')
name_1 = jack.get_name()
print(name_1)