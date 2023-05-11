class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

class Shape:
    def __init__(self, points):
        self.points = points 
    def __str__(self):
        return f"{self.points}"

point_tr_1 = Point(0,0)
point_tr_2 = Point(5,5)
point_tr_3 = Point(2,4)

triangle = Shape([
    point_tr_1, 
    point_tr_2, 
    point_tr_3
    ])

print(triangle) 

point_rec_1 = Point(0,0)
point_rec_2 = Point(10,0)
point_rec_3 = Point(0,10)
point_rec_4 = Point(10,10)

rectangle = Shape([point_rec_1, point_rec_2, point_rec_3, point_rec_4])

print(rectangle) 