#                                     ("\(O_o)/")
class Parallelepiped:
    def __init__(self, x, y, z, width, height, length):
        self.x = x
        self.y = y
        self.z = z
        self.width = width
        self.height = height
        self.length = length

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_z(self):
        return self.z

    def get_width(self):
        return self.width

    def get_height(self):
        return self.height

    def get_length(self):
        return self.length

    def __str__(self):
        return f"""Parallelepiped 
        {
        self.get_x(),
        self.get_y(),
        self.get_z(),
        self.get_width(),
        self.get_height(),
        self.get_length()
        }"""


parallelepiped = Parallelepiped(5, 10, 15, 50, 100, 150)
print(str(parallelepiped))
