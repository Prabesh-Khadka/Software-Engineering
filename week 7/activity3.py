class Circle:
    def draw(self):
        return "Drawing a Circle"

class Square:
    def draw(self):
        return "Drawing a Square"

class NullShape:
    def draw(self):
        return "Unknown shape - nothing to draw"

class ShapeFactory:
    def create_shape(self, shape_type):
        if shape_type == "circle":
            return Circle()
        elif shape_type == "square":
            return Square()
        else:
            return NullShape()  # Return a default shape instead of raising error

factory = ShapeFactory()

shape = factory.create_shape("triangle")  # Returns NullShape instead of error
print(shape.draw())  # Outputs: Unknown shape - nothing to draw

