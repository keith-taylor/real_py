class WrongNumbPoints(Exception):
    def __init__(self, required_numb_points):
        self.required_numb_points= required_numb_points
        
        print(f"\nThis shape does not have the required number of points! \n \nIt needs: {self.required_numb_points} points.\n")

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y
class Shape:
    def __init__(self, points):
        for point in points:
            if not isinstance(point, Points):
                raise TypeError("All items should be members of the Points class.")
        self.points = points

class Square(Shape):
    def __init__(self, points):
        required_numb_points = 4
        if (len(points) != required_numb_points):
            raise WrongNumbPoints(required_numb_points)
        super().__init__(points)
        
class Triangle(Shape):
    def __init__(self, points):
        required_numb_points = 3
        if (len(points) != required_numb_points):
            raise WrongNumbPoints(required_numb_points)
        self.points = points

my_square = Square([
    Points(0,0), 
    Points(0,4), 
    Points(4,4), 
    (4,0)
])        
print(my_square)

