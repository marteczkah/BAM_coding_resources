from random import randint

names = ['Ariya', 'Chandini', 'Kaitlyn', 'Anjali', 'Josephine', 'Zachias',
    'Joel', 'Jayden', 'Larriyah', 'Trevor', 'Kimiwa', 'Suvil', 'Walddy',
    'Eladio', 'Drew', 'Sasha', 'Lauren', 'Neesh', 'Raisha', 'Faye']

random_index = randint(0, len(names) - 1)
print(names[random_index])
