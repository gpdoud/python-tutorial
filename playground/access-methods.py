class Geometry:

    def pi(self):
        return 3.1415
    
class Circle(Geometry):

    def area(self, radius):
        return super().pi() * (radius ** 2)
    
circle = Circle()
area = circle.area(1)
print(area)