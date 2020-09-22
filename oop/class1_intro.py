class Point:
    def draw(self):
        print("draw")


point = Point() # point is an instance of class 'Point'
print(type(point))
point.draw()
print(isinstance(point, Point))
