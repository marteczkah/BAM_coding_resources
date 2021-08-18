# Object Oriented Programming
# Inheritance, Encapsulation, Abstraction, Polymorphism
class Polygon:
    def __init__(self, *sides_length):
        self.sides_number = len(sides_length)
        self.sides_length = sides_length

    def circumference(self):
        circumference = 0 #(cirkumfrenc)
        for side in self.sides_length:
            circumference += side
        return circumference
    
    def sides_num(self):
        return self.sides_number

class Triangle(Polygon):
    def __init__(self, height, a, b, c):
        self.sides_length = (a,b,c)
        self.height = height
    
    def sides_num(self):
        return 3
    
    def area(self):
        return 0.5*self.sides_length[1]*self.height

# add a Square object in a similiar manner

polygon = Polygon(3, 4, 5, 6, 7)
print(polygon.circumference())

triangle = Triangle(10, 15, 15, 15)
print(triangle.sides_num())