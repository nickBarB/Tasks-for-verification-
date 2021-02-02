#                                     ("\(O_o)/")
class Rectangle:
    def __init__(self, a, b):
        self.length = a
        self.width = b
    def rect_area(self):
        return self.length*self.width


rect_for_example = Rectangle(12, 10)
print("The rectangle has an area", rect_for_example.rect_area(), "square centimeters.")
