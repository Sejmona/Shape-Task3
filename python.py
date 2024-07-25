import json

# Základní třída Shape
class Shape:
    def show(self):
        print(self)
    
    def save(self, filename):
        with open(filename, 'w') as f:
            json.dump(self.__dict__, f)
    
    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as f:
            data = json.load(f)
        shape = cls.__new__(cls)
        shape.__dict__.update(data)
        return shape

    def __str__(self):
        return f"{self.__class__.__name__} with attributes {self.__dict__}"

# Třída Square (Čtverec)
class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

# Třída Rectangle (Obdélník)
class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

# Třída Circle (Kružnice)
class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

# Třída Ellipse (Elipsa)
class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

# Vytvoření seznamu tvarů
shapes = [
    Square(1, 1, 5),
    Rectangle(2, 2, 10, 5),
    Circle(5, 5, 3),
    Ellipse(3, 3, 7, 4)
]

# Uložení tvarů do souborů
for i, shape in enumerate(shapes):
    shape.save(f'shape_{i}.json')

# Načtení tvarů ze souborů do nového seznamu
loaded_shapes = []
for i in range(len(shapes)):
    if i == 0:
        loaded_shapes.append(Square.load(f'shape_{i}.json'))
    elif i == 1:
        loaded_shapes.append(Rectangle.load(f'shape_{i}.json'))
    elif i == 2:
        loaded_shapes.append(Circle.load(f'shape_{i}.json'))
    elif i == 3:
        loaded_shapes.append(Ellipse.load(f'shape_{i}.json'))

# Zobrazení informací o načtených tvarech
for shape in loaded_shapes:
    shape.show()
