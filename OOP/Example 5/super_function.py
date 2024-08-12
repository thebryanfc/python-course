#super() = function used to give access to the methods of a parent class.
#          Returns a temporary object of a parent class when used

class Rectangule:
    def __init__(self, length, width):
        self.lenght = length
        self.width = width

class Square(Rectangule):

    def __init__(self, length, width):
        super().__init__(length,width)
    
    def area(self):
        return self.lenght*self.width

class Cube(Rectangule):

    def __init__(self, length, width, height):
        super().__init__(length,width)
        self.height = height
    def volume(self):
        return self.lenght*self.width*self.height

square = Square(3,3)
cube = Cube(3,3,3)  

print(square.area())
print(cube.volume())
